# urls.py
from django.urls import path
from customers.views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

app_name = "customers"

urlpatterns = [
    path("", CustomerListView.as_view(), name="customer-list"),
    path("<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("create/", CustomerCreateView.as_view(), name="customer-create"),
    path(
        "<int:pk>/update/",
        CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "<int:pk>/delete/",
        CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
]
