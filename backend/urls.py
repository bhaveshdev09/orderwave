from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("branch/", include("branches.urls", namespace="branch")),
    path("customer/", include("customers.urls", namespace="customer")),
]
