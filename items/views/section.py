# views.py
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


# Section CRUD
class SectionListView(ListView):
    model = Section
    template_name = "sections/section_list.html"
    context_object_name = "sections"


class SectionDetailView(DetailView):
    model = Section
    template_name = "sections/section_detail.html"
    context_object_name = "section"


class SectionCreateView(CreateView):
    model = Section
    form_class = SectionForm
    template_name = "sections/section_form.html"
    success_url = reverse_lazy("items:section-list")


class SectionUpdateView(UpdateView):
    model = Section
    form_class = SectionForm
    template_name = "sections/section_form.html"
    success_url = reverse_lazy("items:section-list")


class SectionDeleteView(DeleteView):
    model = Section
    template_name = "sections/section_confirm_delete.html"
    success_url = reverse_lazy("items:section-list")
