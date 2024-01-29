from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from users.models import CustomUser
from users.forms import CustomUserForm, CustomUserAuthForm
from django.contrib.auth.views import LogoutView, PasswordResetView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class CustomUserCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user-list")


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("users:user-list")


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user"


class CustomUserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"


class CustomUserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "users/user_confirm_delete.html"
    context_object_name = "user"
    success_url = reverse_lazy("users:user-list")


# Authentication
class CustomLoginView(FormView):
    form_class = CustomUserAuthForm
    template_name = "authentication/login.html"
    success_url = reverse_lazy("analytics:dashboard")  # Adjust 'home' to your home URL

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to=reverse_lazy("analytics:dashboard"))
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            messages.success(self.request, "login successful")
            # Your custom logic after successful login
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        for message in form.errors.values():
            messages.error(
                self.request,
                message[0],
            )

        return response


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been successfully logged out.")
        print("Total:", len(messages.get_messages(self.request)))
        return super().dispatch(request, *args, **kwargs)


# class CustomPasswordResetView(PasswordResetView):
#     template_name = "authentication/password_reset.html"
#     success_url = reverse_lazy(
#         "users:login"
#     )  # Adjust 'password_reset_done' to your reset done URL
