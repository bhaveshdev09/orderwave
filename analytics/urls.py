from django.urls import path
from analytics.views import Dashboard

app_name = "analytics"

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    # path("dashboard/", Dashboard.as_view(), name="dashboard-page"),
]
