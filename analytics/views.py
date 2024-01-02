from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from analytics.models import ProxyPurchseOrder, ProxyCustomer, ProxyVendor, ProxyOrder


# Create your views here.
class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "analytics/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_purchase_orders"] = ProxyPurchseOrder.total_purchase_orders()
        context["total_customers"] = ProxyCustomer.total_customers()
        context["total_vendors"] = ProxyVendor.total_vendors()
        context["total_orders"] = ProxyOrder.total_orders()
        return context
