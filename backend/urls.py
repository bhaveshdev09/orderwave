from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("branch/", include("branches.urls", namespace="branch")),
    path("customer/", include("customers.urls", namespace="customer")),
    path("item/", include("items.urls", namespace="item")),
    path("order/", include("orders.urls", namespace="order")),
    path("", include("users.urls", namespace="user")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
