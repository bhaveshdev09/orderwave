# urls.py
from django.urls import path
from orders.views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
)

app_name = "orders"

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create"),
    path("orders/<int:pk>/update/", OrderUpdateView.as_view(), name="order-update"),
    path("orders/<int:pk>/delete/", OrderDeleteView.as_view(), name="order-delete"),
]
