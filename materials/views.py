from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from materials.models import Material
from materials.forms import MaterialForm


class MaterialListView(ListView):
    model = Material
    template_name = "material/material_list.html"
    context_object_name = "materials"


class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = "materials/material_form.html"
    success_url = reverse_lazy("materials:material-list")


class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = "materials/material_form.html"
    success_url = reverse_lazy("materials:material-list")


class MaterialDeleteView(DeleteView):
    model = Material
    template_name = "materials/material_confirm_delete.html"
    success_url = reverse_lazy("materials:material-list")
