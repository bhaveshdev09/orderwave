from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from branches.models import Branch
from branches.forms import BranchForm


class BranchListView(ListView):
    model = Branch
    template_name = "branch_list.html"
    context_object_name = "branches"
    paginate_by = 5


class BranchDetailView(DetailView):
    model = Branch
    template_name = "branches/branch_detail.html"
    context_object_name = "branch"


class BranchCreateView(CreateView):
    model = Branch
    form_class = BranchForm
    template_name = "branches/branch_form.html"
    success_url = reverse_lazy("branches:branch-list")


class BranchUpdateView(UpdateView):
    model = Branch
    form_class = BranchForm
    template_name = "branches/branch_form.html"
    success_url = reverse_lazy("branches:branch-list")


class BranchDeleteView(DeleteView):
    model = Branch
    template_name = "branches/branch_confirm_delete.html"
    success_url = reverse_lazy("branches:branch-list")
