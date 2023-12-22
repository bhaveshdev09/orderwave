# views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from items.models import Item
from items.forms import ItemForm


class ItemListView(ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item_detail.html"
    context_object_name = "item"


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:item-list")


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "items/item_form.html"
    success_url = reverse_lazy("items:item-list")


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "items/item_confirm_delete.html"
    success_url = reverse_lazy("items:item-list")
