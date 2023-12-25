# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from vendors.models import Vendor
from vendors.forms import VendorForm


class VendorListView(LoginRequiredMixin, ListView):
    model = Vendor
    template_name = "vendors/vendor_list.html"
    context_object_name = "vendors"


class VendorCreateView(LoginRequiredMixin, CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendors/vendor_form.html"
    success_url = reverse_lazy("vendors:vendor-list")


class VendorUpdateView(LoginRequiredMixin, UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendors/vendor_form.html"
    success_url = reverse_lazy("vendors:vendor-list")


class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = Vendor
    template_name = "vendors/vendor_confirm_delete.html"
    success_url = reverse_lazy("vendors:vendor-list")
