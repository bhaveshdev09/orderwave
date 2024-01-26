# urls.py

from django.urls import path
from .views import (
    PurchaseOrderListView,
    PurchaseOrderCreateView,
    PurchaseOrderUpdateView,
    PurchaseOrderDeleteView,
    PurchaseOrderExportToExcelView,
    TogglePurchaseOrderStatusView,
)

app_name = "purchase_orders"

urlpatterns = [
    path("", PurchaseOrderListView.as_view(), name="purchase-order-list"),
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
    path(
        "export/",
        PurchaseOrderExportToExcelView.as_view(),
        name="export-purchase-orders-to-excel",
    ),
    path(
        "<int:pk>/update-status/",
        TogglePurchaseOrderStatusView.as_view(),
        name="toggle_purchase_order_status",
    ),
]
