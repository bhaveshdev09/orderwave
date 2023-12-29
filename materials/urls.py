from django.urls import path
from materials.views import (
    MaterialListView,
    MaterialCreateView,
    MaterialUpdateView,
    MaterialDeleteView,
)

app_name = "materials"

urlpatterns = [
    path("", MaterialListView.as_view(), name="material-list"),
    path("create/", MaterialCreateView.as_view(), name="material-create"),
    path(
        "<int:pk>/update/",
        MaterialUpdateView.as_view(),
        name="material-update",
    ),
    path(
        "<int:pk>/delete/",
        MaterialDeleteView.as_view(),
        name="material-delete",
    ),
]
