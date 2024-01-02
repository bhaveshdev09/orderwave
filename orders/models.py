from collections.abc import Iterable
from django.db import models
from django.utils import timezone
from backend.models import BaseModel
from items.models import Item
from customers.models import Customer


class Order(BaseModel):
    order_no = models.CharField(max_length=20, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0)
    total_price = models.FloatField(default=0, editable=False)
    is_deleted = models.BooleanField(default=False)

    @property
    def total(self):
        return sum(order_item.total_price for order_item in self.order_set.all())

    @property
    def final_total(self):
        return self.total - self.discount

    def __str__(self):
        return f"CC-{self.order_date.strftime('%d%m%Y')}-{self.order_no}"

    @property
    def order_repr(self) -> str:
        return f"CC-{self.order_date.strftime('%d%m%Y')}-{self.order_no}"

    def save(self, *args, **kwargs) -> None:
        new_order_id = self._meta.model.objects.count() + 1
        self.order_no = str(new_order_id)
        # filter_orderitems = OrderItem.objects.filter(order=self)

        # self.total_price = filter_orderitems.aggregate(
        #     total_price=models.Sum("total_price")
        # ).get("total_price")
        # self.total_price = 0 if not self.total_price else self.total_price

        return super().save(*args, **kwargs)


class OrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.FloatField(editable=False)
    order = models.ForeignKey(Order, related_name="items", on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        # Calculate total price before saving
        self.total_price = self.item.base_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item: {self.item.name}, Quantity: {self.quantity}"


class Bill(BaseModel):
    # Bill Status
    STATUS_CHOICE_PENDING = "pending"
    STATUS_CHOICE_COMPLETE = "complete"
    STATUS_CHOICES = [
        ("complete", "Complete"),
        ("pending", "Pending"),
    ]

    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, default=None, null=True
    )
    # train_number = models.JSONField()  # Assuming you're using Django 3.1+
    train_number = models.CharField(max_length=255, blank=True, default="-")
    train_name = models.CharField(max_length=255, blank=True, default="-")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, default=None, null=True
    )
    bill_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Bill for Order: Customer: {self.customer.name}, Status: {self.status}"

    @property
    def order_repr(self) -> str:
        return f"CC-{self.bill_date.strftime('%d%m%Y')}-{self.order.order_no}"
