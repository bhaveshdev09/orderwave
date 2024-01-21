# urls.py
from django.urls import path
from orders.views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    BillListView,
    BillCreateView,
    BillUpdateView,
    BillDeleteView,
    BillsExportToExcelView,
)

app_name = "orders"

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order-update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
    path("bills/", BillListView.as_view(), name="bill-list"),
    path("bills/create/", BillCreateView.as_view(), name="bill-create"),
    path("bills/<int:pk>/update/", BillUpdateView.as_view(), name="bill-update"),
    path("bills/<int:pk>/delete/", BillDeleteView.as_view(), name="bill-delete"),
    path("export/", BillsExportToExcelView.as_view(), name="export-bills-to-excel"),
    # Add any other URLs as needed.
]
