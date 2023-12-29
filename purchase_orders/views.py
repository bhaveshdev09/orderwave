from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PurchaseOrder
from .forms import PurchaseOrderForm


class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = "purchase_orders/purchase_order_list.html"
    context_object_name = "purchase_orders"


class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = "purchase_orders/purchase_order_form.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")


class PurchaseOrderUpdateView(UpdateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = "purchase_orders/purchase_order_form.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")


class PurchaseOrderDeleteView(DeleteView):
    model = PurchaseOrder
    template_name = "purchase_orders/purchase_order_confirm_delete.html"
    success_url = reverse_lazy("purchase_orders:purchase-order-list")
    context_object_name = "purchase_order"
