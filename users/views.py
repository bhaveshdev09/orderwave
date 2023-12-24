from django.contrib.auth.mixins import LoginRequiredMixin
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
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


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
    success_url = reverse_lazy("users:user-list")  # Adjust 'home' to your home URL

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, email=email, password=password)

        if user is not None:
            login(self.request, user)
            # Your custom logic after successful login
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(form.errors.as_data())
        response = super().form_invalid(form)
        return response


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


# class CustomPasswordResetView(PasswordResetView):
#     template_name = "authentication/password_reset.html"
#     success_url = reverse_lazy(
#         "users:login"
#     )  # Adjust 'password_reset_done' to your reset done URL
