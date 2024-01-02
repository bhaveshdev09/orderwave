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


# class BillCreateView(CreateView):
#     model = Bill
#     form_class = BillForm
#     template_name = "bills/bill_form.html"
#     success_url = reverse_lazy("orders:bill-list")

#     def form_invalid(self, form):
#         print(form.errors)
#         response = super().form_invalid(form)
#         return response


class BillCreateView(CreateView):
    model = Bill
    form_class = BillForm
    template_name = "bills/bill_form.html"
    success_url = reverse_lazy("orders:bill-list")

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

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class BillUpdateView(UpdateView):
    model = Bill
    template_name = "bills/bill_form.html"
    form_class = BillForm

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

    # def form_valid(self, form):
    #     bill_instance = form.save(commit=False)

    #     # Update the attributes of the Order instance if needed
    #     # For example, bill_instance.order.attribute_name = form.cleaned_data['some_field']

    #     # Save the changes to the Order instance
    #     bill_instance.order.save()

    #     # Save the changes to the Bill instance
    #     bill_instance.save()

    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("orders:bill-list")


class BillDeleteView(DeleteView):
    model = Bill
    template_name = "bills/bill_confirm_delete.html"
    success_url = reverse_lazy("orders:bill-list")
