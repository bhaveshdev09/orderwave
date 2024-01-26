from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from analytics.models import (
    ProxyPurchaseOrder,
    ProxyCustomer,
    ProxyVendor,
    ProxyOrder,
)
from django.http import JsonResponse
from django.db.models import Subquery, Sum
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from datetime import timedelta


# Create your views here.
class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "analytics/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_purchase_orders"] = ProxyPurchaseOrder.total_purchase_orders()
        context[
            "total_purchase_orders_value"
        ] = ProxyPurchaseOrder.total_purchase_order_value()
        context["total_orders_value"] = ProxyOrder.total_order_value()
        context["total_orders"] = ProxyOrder.total_orders()
        return context


# TODO: Needs Optimization in the view logic


class DashboardAPIView(View):
    def get(self, request, *args, **kwargs):
        interval = request.GET.get("interval", "weekly")
        timerange_list = self.get_timerange_list(interval)

        _total_sales_data, _total_purchase_data = self.get_weekly_data(
            timerange_list, interval
        )

        if interval == "monthly":
            timerange_list = [each.strftime("%Y-%m") for each in timerange_list]

        context = {
            "income_data": _total_sales_data,
            "expense_data": _total_purchase_data,
            "labels": timerange_list,
        }
        return JsonResponse(context, safe=True)

    def get_timerange_list(self, interval):
        d = timezone.now().date()
        timerange_list = []

        if interval == "weekly":
            timerange_list = [
                (d + timedelta(days=-i)).isoformat() for i in range(6, -1, -1)
            ]
        elif interval == "monthly":
            timerange_list = [(d + relativedelta(months=-i)) for i in range(11, -1, -1)]

        return timerange_list

    def get_weekly_data(self, timerange_list, interval):
        _total_sales_data = []
        _total_purchase_data = []

        for tr in timerange_list:
            if interval == "weekly":
                purchases_data = ProxyPurchaseOrder.objects.filter(order_date__date=tr)
                sales_data = ProxyOrder.objects.filter(bill_date__date=tr)
            else:
                purchases_data = ProxyPurchaseOrder.objects.filter(
                    order_date__date__month=tr.month, order_date__date__year=tr.year
                )
                sales_data = ProxyOrder.objects.filter(
                    bill_date__date__month=tr.month, bill_date__date__year=tr.year
                )

            _total_sales_data.append(sum([i.total for i in sales_data]))

            _total_purchase_data.append(-sum([i.total_cost for i in purchases_data]))

        return _total_sales_data, _total_purchase_data


# class DashboardAPIView(View):
#     def get(self, request, *args, **kwargs):
#         interval = request.GET.get("interval", "weekly")
#         # weekly timeframe last 7 days
#         from django.utils import timezone
#         from datetime import date, timedelta
#         from dateutil.relativedelta import relativedelta

#         d = timezone.now().date()
#         timerange_list = []
#         if interval == "weekly":
#             timerange_list = [
#                 (d + timedelta(days=-i)).isoformat() for i in range(6, -1, -1)
#             ]
#         elif interval == "monthly":
#             timerange_list = [(d + relativedelta(months=-i)) for i in range(11, -1, -1)]

#         # timerange_list =  [
#         #     (d + timedelta(days=-i)).isoformat() for i in range(6, -1, -1)
#         # ]
#         if timerange_list:
#             if interval == "weekly":
#                 purchases_data = ProxyPurchseOrder.objects.filter(
#                     order_date__date__range=(
#                         timerange_list[0],
#                         timerange_list[-1],
#                     )  # + timedelta(days=-1)
#                 )
#                 sales_data = ProxyOrder.objects.filter(
#                     bill_date__date__range=(
#                         timerange_list[0],
#                         timerange_list[-1],
#                     )
#                 )
#                 weekly_total_sales_data = [
#                     sum([i.total for i in sales_data.filter(bill_date__date=tr)])
#                     for tr in timerange_list
#                 ]
#                 weekly_total_purchase_data = [
#                     -(
#                         sum(
#                             [
#                                 i.total_cost
#                                 for i in purchases_data.filter(order_date__date=tr)
#                             ]
#                         )
#                     )
#                     for tr in timerange_list
#                 ]
#             else:
#                 # purchases_data = ProxyPurchseOrder.objects.filter(
#                 #     order_date__date__month__range=(
#                 #         timerange_list[0].month,
#                 #         timerange_list[-1].month,
#                 #     ),
#                 #     order_date__date__year__range=(
#                 #         timerange_list[0].year,
#                 #         timerange_list[-1].year,
#                 #     ),  # + timedelta(days=-1)
#                 # )
#                 # print(purchases_data)
#                 # sales_data = Bill.objects.filter(
#                 #     bill_date__date__month__range=(
#                 #         timerange_list[0].month,
#                 #         timerange_list[-1].month,
#                 #     ),
#                 #     bill_date__date__year__range=(
#                 #         timerange_list[0].year,
#                 #         timerange_list[-1].year,
#                 #     ),
#                 # )
#                 # print(sales_data)
#                 weekly_total_sales_data = [
#                     sum(
#                         [
#                             i.total
#                             for i in ProxyOrder.objects.filter(
#                                 bill_date__date__month=tr.month,
#                                 bill_date__date__year=tr.year,
#                             )
#                         ]
#                     )
#                     for tr in timerange_list
#                 ]
#                 weekly_total_purchase_data = [
#                     -(
#                         sum(
#                             [
#                                 i.total_cost
#                                 for i in ProxyPurchseOrder.objects.filter(
#                                     order_date__date__month=tr.month,
#                                     order_date__date__year=tr.year,
#                                 )
#                             ]
#                         )
#                     )
#                     for tr in timerange_list
#                 ]
#                 timerange_list = [
#                     (d + relativedelta(months=-i)).strftime("%Y-%m")
#                     for i in range(11, -1, -1)
#                 ]
#         else:
#             weekly_total_purchase_data = []
#             weekly_total_sales_data = []

#         context = {
#             "income_data": weekly_total_sales_data,
#             "expense_data": weekly_total_purchase_data,
#             "labels": timerange_list,
#         }
#         return JsonResponse(context, safe=True)
