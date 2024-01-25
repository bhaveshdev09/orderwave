from django.urls import path
from analytics.views import Dashboard, DashboardAPIView

app_name = "analytics"

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path("api/transactions/", DashboardAPIView.as_view(), name="dashboard-bar-api"),
    # path("dashboard/", Dashboard.as_view(), name="dashboard-page"),
]
