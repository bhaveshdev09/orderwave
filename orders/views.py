from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.urls import reverse_lazy
from orders.models import Order, OrderItem, Bill
from orders.forms import OrderForm, BillForm
from items.models import Item
from django.contrib.messages.views import SuccessMessageMixin


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


class BillListView(ListView):
    model = Bill
    template_name = "bills/bill_list.html"
    context_object_name = "bills"


class BillCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Bill
    form_class = BillForm
    template_name = "bills/bill_form.html"
    success_url = reverse_lazy("orders:bill-list")
    success_message = "Order created successfully."

    # def form_valid(self, form):
    #     # The code `print(self.request.POST)` is printing the POST data that is submitted with the
    #     # form. This can be useful for debugging purposes to see the data that is being sent to the
    #     # server.
    #     form.save()
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs: Any):
        self.context = super().get_context_data(**kwargs)
        self.context["items"] = list(
            Item.objects.only(
                "id", "name", "base_price", "tax", "selling_price"
            ).values("id", "name", "base_price", "tax")
        )
        return self.context

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
