from purchase_orders.models import PurchaseOrder
from customers.models import Customer
from vendors.models import Vendor
from orders.models import Order, Bill


# Create your models here.
class ProxyPurchseOrder(PurchaseOrder):
    class Meta:
        proxy = True

    @classmethod
    def total_purchase_orders(cls):
        return cls._default_manager.count()


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

