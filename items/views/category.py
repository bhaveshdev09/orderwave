# views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from items.models.category import Category
from items.forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories/category_detail.html"
    context_object_name = "category"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("items:category-list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("items:category-list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/category_confirm_delete.html"
    success_url = reverse_lazy("items:category-list")
