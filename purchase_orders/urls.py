# urls.py

from django.urls import path
from .views import (
    PurchaseOrderListView,
    PurchaseOrderCreateView,
    PurchaseOrderUpdateView,
    PurchaseOrderDeleteView,
)

app_name = "purchase_orders"

urlpatterns = [
    path(
        "", PurchaseOrderListView.as_view(), name="purchase-order-list"
    ),
    path(
        "create/",
        PurchaseOrderCreateView.as_view(),
        name="purchase-order-create",
    ),
    path(
        "<int:pk>/update/",
        PurchaseOrderUpdateView.as_view(),
        name="purchase-order-update",
    ),
    path(
        "<int:pk>/delete/",
        PurchaseOrderDeleteView.as_view(),
        name="purchase-order-delete",
    ),
]
