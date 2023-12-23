# users/urls.py
from django.urls import path
from users.views import (
    CustomUserListView,
    CustomUserDetailView,
    CustomUserCreateView,
    CustomUserUpdateView,
    CustomUserDeleteView,
)

app_name = "users"

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", CustomUserDetailView.as_view(), name="user-detail"),
    path("users/create/", CustomUserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", CustomUserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", CustomUserDeleteView.as_view(), name="user-delete"),
]
