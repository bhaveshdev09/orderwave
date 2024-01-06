from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from materials.models import Material
from materials.forms import MaterialForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    template_name = "material/material_list.html"
    context_object_name = "materials"


class MaterialCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Material
    form_class = MaterialForm
    template_name = "materials/material_form.html"
    success_url = reverse_lazy("materials:material-list")
    success_message = "Material created successfully."

    def form_invalid(self, form):
        print(form.errors)
        response = super().form_invalid(form)
        return response


class MaterialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = "materials/material_form.html"
    success_url = reverse_lazy("materials:material-list")
    success_message = "Material updated successfully."


class MaterialDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Material
    template_name = "materials/material_confirm_delete.html"
    success_url = reverse_lazy("materials:material-list")
    success_message = "Material deleted successfully."
