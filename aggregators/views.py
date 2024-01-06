from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from aggregators.models import Aggregator
from aggregators.forms import AggregatorForm


class AggregatorListView(LoginRequiredMixin, ListView):
    model = Aggregator
    template_name = "aggregator_list.html"
    context_object_name = "aggregators"
    paginate_by = 5


class AggregatorDetailView(LoginRequiredMixin, DetailView):
    model = Aggregator
    template_name = "aggregators/aggregator_detail.html"
    context_object_name = "aggregator"


class AggregatorCreateView(LoginRequiredMixin, CreateView):
    model = Aggregator
    form_class = AggregatorForm
    template_name = "aggregators/aggregator_form.html"
    success_url = reverse_lazy("aggregators:aggregator-list")

    def form_valid(self, form):
        print(self.request.user)
        return super().form_valid(form)


class AggregatorUpdateView(LoginRequiredMixin, UpdateView):
    model = Aggregator
    form_class = AggregatorForm
    template_name = "aggregators/aggregator_form.html"
    success_url = reverse_lazy("aggregators:aggregator-list")


class AggregatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Aggregator
    template_name = "aggregators/aggregator_confirm_delete.html"
    success_url = reverse_lazy("aggregators:aggregator-list")
