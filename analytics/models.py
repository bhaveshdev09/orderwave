from purchase_orders.models import PurchaseOrder, PurchaseOrderItem
from customers.models import Customer
from vendors.models import Vendor
from orders.models import Order, Bill, OrderItem
from django.db.models import Sum


# Create your models here.
class ProxyPurchaseOrder(PurchaseOrder):
    class Meta:
        proxy = True

    @classmethod
    def total_purchase_orders(cls):
        return cls._default_manager.count()

    @classmethod
    def total_purchase_order_value(cls):
        return (
            PurchaseOrderItem.objects.all()
            .aggregate(total=Sum("total_price", default=0))
            .get("total")
        )


class ProxyCustomer(Customer):
    class Meta:
        proxy = True

    @classmethod
    def total_customers(cls):
        return cls._default_manager.count()


class ProxyVendor(Vendor):
    class Meta:
        proxy = True

    @classmethod
    def total_vendors(cls):
        return cls._default_manager.count()


class ProxyOrder(Bill):
    class Meta:
        proxy = True

    @classmethod
    def total_orders(cls):
        return cls._default_manager.count()

    @classmethod
    def total_order_value(cls):
        return (
            OrderItem.objects.all()
            .aggregate(total=Sum("total_price", default=0))
            .get("total")
        )
