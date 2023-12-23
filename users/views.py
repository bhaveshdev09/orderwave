from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from users.models import CustomUser
from users.forms import CustomUserForm


class CustomUserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user-list")


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user-list")


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user"


class CustomUserListView(ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = "users/user_confirm_delete.html"
    context_object_name = "user"
    success_url = reverse_lazy("users:user-list")
