from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from purchase_orders.models import PurchaseOrder, Material
from purchase_orders.forms import PurchaseOrderForm
from purchase_orders.resources import PurchaseOrderResource
from import_export.mixins import ExportViewMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404


class PurchaseOrderListView(LoginRequiredMixin, ListView):
    model = PurchaseOrder
    template_name = "purchase_orders/purchase_order_list.html"
    context_object_name = "purchase_orders"
    queryset = PurchaseOrder.objects.all().order_by("-created_at")

    def get(self, request, *args, **kwargs):
        status = request.GET.get("status", None)
        if status in (
            PurchaseOrder.STATUS_CHOICE_PENDING,
            PurchaseOrder.STATUS_CHOICE_COMPLETE,
        ):
            self.queryset = self.queryset.filter(status=status)
        return super().get(request, *args, **kwargs)


class PurchaseOrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = "purchase_orders/purchase_order_form.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")
    success_message = "Purchase Order created successfully."

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Material.objects.only("id", "name", "price").values("id", "name", "price")
        )
        return self.context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.order_branch = self.request.user.assigned_branch
        return super().form_valid(form)


class PurchaseOrderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = "purchase_orders/purchase_order_form.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")
    success_message = "Purchase Order updated successfully."

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Material.objects.only("id", "name", "price").values("id", "name", "price")
        )
        return self.context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PurchaseOrderDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PurchaseOrder
    template_name = "purchase_orders/purchase_order_confirm_delete.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")
    context_object_name = "purchase_order"
    success_message = "Purchase Order deleted successfully."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PurchaseOrderExportToExcelView(ExportViewMixin, View):
    model = PurchaseOrder
    resource_class = PurchaseOrderResource  # Use the default ModelResource

    def get(self, request, *args, **kwargs):
        # Export the data to Excel
        dataset = self.resource_class().export()
        from django.http import HttpResponse

        response = HttpResponse(
            dataset.xlsx,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response[
            "Content-Disposition"
        ] = "attachment; filename=purchase_orders_export.xlsx"

        return response


# API
class TogglePurchaseOrderStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        except Http404:
            # messages.error(request, "Invalid request")
            return JsonResponse({"status": "error", "message": "Invalid request"})
        # Toggle the status
        if purchase_order.status == PurchaseOrder.STATUS_CHOICE_PENDING:
            purchase_order.status = PurchaseOrder.STATUS_CHOICE_COMPLETE
        else:
            purchase_order.status = PurchaseOrder.STATUS_CHOICE_PENDING

        purchase_order.save()
        # messages.success(request, "Order status updated")
        return JsonResponse(
            {
                "status": "success",
                "message": "Purchase order status updated",
                "purchase_order_current_status": purchase_order.status,
            }
        )
