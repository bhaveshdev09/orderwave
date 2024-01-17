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

from items.views.operatinghour import (
    OperatingHourListView,
    OperatingHourDetailView,
    OperatingHourUpdateView,
    # OperatingHourDeleteView,
    # OperatingHourCreateView,
)
from items.views.item import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
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
    # URL Patterns For Operating Hours
    path(
        "operating-hours/", OperatingHourListView.as_view(), name="operating-hour-list"
    ),
    path(
        "operating-hours/<int:pk>/",
        OperatingHourDetailView.as_view(),
        name="operating-hour-detail",
    ),
    path(
        "operating-hours/<int:pk>/update/",
        OperatingHourUpdateView.as_view(),
        name="operating-hour-update",
    ),
    # TODO: future use case
    # path(
    #     "operating-hours/create/",
    #     OperatingHourCreateView.as_view(),
    #     name="operating-hour-create",
    # ),
    # path(
    #     "operating-hours/<int:pk>/delete/",
    #     OperatingHourDeleteView.as_view(),
    #     name="operating-hour-delete",
    # ),
    # URL Patterns For Item
    path("", ItemListView.as_view(), name="item-list"),
    path("<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("create/", ItemCreateView.as_view(), name="item-create"),
    path("<int:pk>/update/", ItemUpdateView.as_view(), name="item-update"),
    path("<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
]
