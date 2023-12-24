# users/urls.py
from django.urls import path
from users.views import (
    CustomUserListView,
    CustomUserDetailView,
    CustomUserCreateView,
    CustomUserUpdateView,
    CustomUserDeleteView,
    CustomLoginView,
    CustomLogoutView,
    # CustomPasswordResetView,
)


urlpatterns = []


app_name = "users"

urlpatterns = [
    path("users/", CustomUserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", CustomUserDetailView.as_view(), name="user-detail"),
    path("users/create/", CustomUserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/details/", CustomUserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", CustomUserDeleteView.as_view(), name="user-delete"),
    # Authentication
    # Your other URL patterns
    path(
        "login/",
        CustomLoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        CustomLogoutView.as_view(),
        name="logout",
    ),
    # path(
    #     "change-password/",
    #     CustomPasswordResetView.as_view(),
    #     name="password_change",
    # ),
]
