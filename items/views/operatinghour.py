from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from items.models import OperatingHour
from items.forms import OperatingHourForm
from django.contrib.messages.views import SuccessMessageMixin


class OperatingHourListView(LoginRequiredMixin, ListView):
    model = OperatingHour
    template_name = "operatinghour/operatinghour_list.html"
    context_object_name = "operatinghours"


class OperatingHourDetailView(LoginRequiredMixin, DetailView):
    model = OperatingHour
    template_name = "operatinghour/operatinghour_detail.html"
    context_object_name = "operatinghour"


class OperatingHourUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = OperatingHour
    form_class = OperatingHourForm
    template_name = "operatinghour/operatinghour_form.html"
    success_url = reverse_lazy("items:operating-hour-list")
    success_message = "Operating hour updated successfully."

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# TODO:future use case
# class OperatingHourCreateView(CreateView):
#     model = OperatingHour
#     form_class = OperatingHourForm
#     template_name = "operatinghour/operatinghour_form.html"
#     success_url = reverse_lazy("items:operating-hour-list")


# TODO: Future use case
# class OperatingHourDeleteView(DeleteView):
#     model = OperatingHour
#     template_name = "operatinghour/operatinghour_confirm_delete.html"
#     success_url = reverse_lazy("items:operating-hour-list")
