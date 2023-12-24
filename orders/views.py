# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView,
# )
# from django.urls import reverse_lazy
# from orders.models import Order
# from orders.forms import OrderForm


# class OrderListView(ListView):
#     model = Order
#     template_name = "orders/order_list.html"
#     context_object_name = "orders"


# class OrderDetailView(DetailView):
#     model = Order
#     template_name = "orders/order_detail.html"
#     context_object_name = "order"


# class OrderCreateView(CreateView):
#     model = Order
#     form_class = OrderForm
#     template_name = "orders/order_form.html"
#     success_url = reverse_lazy("orders:order-list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         return response


# class OrderUpdateView(UpdateView):
#     model = Order
#     form_class = OrderForm
#     template_name = "orders/order_form.html"
#     success_url = reverse_lazy("orders:order-list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         return response


# class OrderDeleteView(DeleteView):
#     model = Order
#     template_name = "orders/order_confirm_delete.html"
#     success_url = reverse_lazy("orders:order-list")


# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Order, OrderItem
from .forms import OrderForm


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
