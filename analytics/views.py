from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "analytics/dashboard.html"
