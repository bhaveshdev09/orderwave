# urls.py
from django.urls import path
from branches.views import (
    BranchListView,
    BranchDetailView,
    BranchCreateView,
    BranchUpdateView,
    BranchDeleteView,
)

app_name = "branches"

urlpatterns = [
    path("", BranchListView.as_view(), name="branch-list"),
    path("<int:pk>/", BranchDetailView.as_view(), name="branch-detail"),
    path("create/", BranchCreateView.as_view(), name="branch-create"),
    path("<int:pk>/update/", BranchUpdateView.as_view(), name="branch-update"),
    path("<int:pk>/delete/", BranchDeleteView.as_view(), name="branch-delete"),
]
