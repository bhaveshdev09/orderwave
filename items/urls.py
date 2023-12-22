from django.urls import path
from items.views.section import (
    SectionListView,
    SectionDetailView,
    SectionCreateView,
    SectionUpdateView,
    SectionDeleteView,
)
from items.views.category import (
    CategoryCreateView,
    CategoryDetailView,
    CategoryListView,
    CategoryDeleteView,
    CategoryUpdateView,
)


app_name = "items"
urlpatterns = [
    # URL Patterns For Section
    path("sections/", SectionListView.as_view(), name="section-list"),
    path("sections/<int:pk>/", SectionDetailView.as_view(), name="section-detail"),
    path("sections/create/", SectionCreateView.as_view(), name="section-create"),
    path(
        "sections/<int:pk>/update/", SectionUpdateView.as_view(), name="section-update"
    ),
    path(
        "sections/<int:pk>/delete/", SectionDeleteView.as_view(), name="section-delete"
    ),

    # URL Patterns For Category
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("categories/create/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "categories/<int:pk>/update/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
]
