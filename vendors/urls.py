# urls.py
from django.urls import path
from vendors.views import (
    VendorListView,
    VendorCreateView,
    VendorUpdateView,
    VendorDeleteView,
)

app_name = "vendors"

urlpatterns = [
    path("", VendorListView.as_view(), name="vendor-list"),
    path("create/", VendorCreateView.as_view(), name="vendor-create"),
    path("update/<int:pk>/", VendorUpdateView.as_view(), name="vendor-update"),
    path("delete/<int:pk>/", VendorDeleteView.as_view(), name="vendor-delete"),
]
