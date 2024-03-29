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
    path("suppliers/", include("vendors.urls", namespace="vendor")),
    path("materials/", include("materials.urls", namespace="material")),
    path(
        "purchase-orders/", include("purchase_orders.urls", namespace="purchase_order")
    ),
    path("aggregators/", include("aggregators.urls", namespace="aggregator")),
    path("", include("users.urls", namespace="user")),
    path("", include("analytics.urls", namespace="analytics")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
