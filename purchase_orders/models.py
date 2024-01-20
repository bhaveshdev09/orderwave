from django.db import models
from django.utils import timezone
from backend.models import BaseModel
from vendors.models import Vendor
from materials.models import Material


class PurchaseOrder(BaseModel):
    STATUS_CHOICES = [
        ("complete", "Complete"),
        ("incomplete", "Incomplete"),
    ]

    po_no = models.CharField(max_length=20, editable=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    total = models.FloatField(default=0, editable=False)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="incomplete"
    )

    def __str__(self):
        return f"PO-{self.order_date.strftime('%d%m%Y')}-{self.po_no}"

    @property
    def purchase_order_id(self):
        return f"PO-{self.order_date.strftime('%d%m%Y')}-{self.pk}"

    def get_total(self):
        return (
            self.materials.all()
            .aggregate(total=models.Sum("total_price", default=0))
            .get("total")
        )

    @property
    def total_cost(self):
        return self.get_total()

    def save(self, *args, **kwargs):
        new_po_id = self._meta.model.objects.count() + 1
        self.po_no = str(new_po_id)
        super().save(*args, **kwargs)


class PurchaseOrderItem(BaseModel):
    material = models.ForeignKey(
        Material, on_delete=models.SET_NULL, null=True, blank=True
    )
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.FloatField(editable=False)
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        related_name="materials",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Calculate total price before saving
        self.total_price = self.material.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Item: {self.material.name}, Quantity: {self.quantity}"
