from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from purchase_orders.models import PurchaseOrder, Material
from purchase_orders.forms import PurchaseOrderForm
from purchase_orders.resources import PurchaseOrderResource
from import_export.mixins import ExportViewMixin


class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = "purchase_orders/purchase_order_list.html"
    context_object_name = "purchase_orders"


class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = "purchase_orders/purchase_order_form.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Material.objects.only("id", "name", "price").values("id", "name", "price")
        )
        print(self.context)
        return self.context


class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = "purchase_orders/purchase_order_form.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Material.objects.only("id", "name", "price").values("id", "name", "price")
        )
        print(self.context)
        return self.context


class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    template_name = "purchase_orders/purchase_order_confirm_delete.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")
    context_object_name = "purchase_order"


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
