# urls.py
from django.urls import path
from aggregators.views import (
    AggregatorListView,
    AggregatorCreateView,
    AggregatorUpdateView,
    AggregatorDetailView,
    AggregatorDeleteView,
)

app_name = "aggregators"

urlpatterns = [
    path("", AggregatorListView.as_view(), name="aggregator-list"),
    path("<int:pk>/", AggregatorDetailView.as_view(), name="aggregator-detail"),
    path("create/", AggregatorCreateView.as_view(), name="aggregator-create"),
    path("<int:pk>/update/", AggregatorUpdateView.as_view(), name="aggregator-update"),
    path("<int:pk>/delete/", AggregatorDeleteView.as_view(), name="aggregator-delete"),
]
