from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from items.models.section import Section
from items.forms import SectionForm
from django.contrib.messages.views import SuccessMessageMixin


# Section CRUD
class SectionListView(LoginRequiredMixin, ListView):
    model = Section
    template_name = "sections/section_list.html"
    context_object_name = "sections"


class SectionDetailView(LoginRequiredMixin, DetailView):
    model = Section
    template_name = "sections/section_detail.html"
    context_object_name = "section"


class SectionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Section
    form_class = SectionForm
    template_name = "sections/section_form.html"
    success_url = reverse_lazy("items:section-list")
    success_message = "Section created successfully."


class SectionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Section
    form_class = SectionForm
    template_name = "sections/section_form.html"
    success_url = reverse_lazy("items:section-list")
    success_message = "Section updated successfully."


class SectionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Section
    template_name = "sections/section_confirm_delete.html"
    success_url = reverse_lazy("items:section-list")
    success_message = "Section deleted successfully."