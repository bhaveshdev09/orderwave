from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
    View,
)
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse, Http404
from orders.models import Order, OrderItem, Bill
from orders.forms import OrderForm, BillForm
from items.models import Item
from django.contrib.messages.views import SuccessMessageMixin
from import_export.mixins import ExportViewMixin
from orders.resources import BillResource

from django.contrib import messages


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/order_list.html"
    context_object_name = "orders"


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/order_detail.html"
    context_object_name = "order"


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:order-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "orders/order_form.html"
    success_url = reverse_lazy("orders:order-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/order_confirm_delete.html"
    success_url = reverse_lazy("orders:order-list")


class BillListView(LoginRequiredMixin, ListView):
    model = Bill
    template_name = "bills/bill_list.html"
    context_object_name = "bills"
    queryset = Bill.objects.all().order_by(
        "-created_at"
    )  # TODO: Bill Orders are not ordering by created at

    def get(self, request, *args, **kwargs):
        status = request.GET.get("status", None)
        if status in (Bill.STATUS_CHOICE_PENDING, Bill.STATUS_CHOICE_COMPLETE):
            self.queryset = self.queryset.filter(status=status)
        return super().get(request, *args, **kwargs)


class BillCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Bill
    form_class = BillForm
    template_name = "bills/bill_form.html"
    success_url = reverse_lazy("orders:bill-list")
    success_message = "Order created successfully."

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Item.objects.only(
                "id", "name", "base_price", "tax", "selling_price"
            ).values("id", "name", "base_price", "tax")
        )
        return self.context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.order_branch = self.request.user.assigned_branch
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class BillUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Bill
    template_name = "bills/bill_form.html"
    form_class = BillForm
    context_object_name = "order"
    success_message = "Order updated successfully."

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related("order", "customer")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Item.objects.only(
                "id", "name", "base_price", "tax", "selling_price"
            ).values("id", "name", "base_price", "tax")
        )
        return self.context

    def get_success_url(self):
        return reverse_lazy("orders:bill-list")


class BillDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Bill
    template_name = "bills/bill_confirm_delete.html"
    success_url = reverse_lazy("orders:bill-list")
    success_message = "Order deleted successfully."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BillsExportToExcelView(ExportViewMixin, View):
    model = Bill
    resource_class = BillResource  # Use the default ModelResource

    def get(self, request, *args, **kwargs):
        # Export the data to Excel
        dataset = BillResource().export()
        from django.http import HttpResponse

        response = HttpResponse(
            dataset.xlsx,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = "attachment; filename=bills_export.xlsx"

        return response


# API
class ToggleBillStatusView(LoginRequiredMixin, View):
    def post(self, request, pk):
        try:
            bill = get_object_or_404(Bill, pk=pk)
        except Http404:
            # messages.error(request, "Invalid request")
            return JsonResponse({"status": "error", "message": "Invalid request"})
        # Toggle the status
        if bill.status == Bill.STATUS_CHOICE_PENDING:
            bill.status = Bill.STATUS_CHOICE_COMPLETE
        else:
            bill.status = Bill.STATUS_CHOICE_PENDING

        bill.save()
        # messages.success(request, "Order status updated")
        return JsonResponse(
            {
                "status": "success",
                "message": "Order status updated",
                "bill_current_status": bill.status,
            }
        )
