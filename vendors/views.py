# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from vendors.models import Vendor
from vendors.forms import VendorForm
from django.contrib.messages.views import SuccessMessageMixin


class VendorListView(LoginRequiredMixin, ListView):
    model = Vendor
    template_name = "vendors/vendor_list.html"
    context_object_name = "vendors"


class VendorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendors/vendor_form.html"
    success_url = reverse_lazy("vendors:vendor-list")
    success_message = "Vendor created successfully."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class VendorUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Vendor
    form_class = VendorForm
    template_name = "vendors/vendor_form.html"
    success_url = reverse_lazy("vendors:vendor-list")
    success_message = "Vendor updated successfully."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class VendorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Vendor
    template_name = "vendors/vendor_confirm_delete.html"
    success_url = reverse_lazy("vendors:vendor-list")
    success_message = "Vendor deleted successfully."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
