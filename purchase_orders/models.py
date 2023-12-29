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
    material = models.ManyToManyField(Material)
    total = models.FloatField(default=0, editable=False)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="incomplete"
    )

    def __str__(self):
        return f"PO-{self.order_date.strftime('%d%m%Y')}-{self.po_no}"

    @property
    def purchase_order_id(self):
        return f"PO-{self.order_date.strftime('%d%m%Y')}-{self.po_no}"

    def save(self, *args, **kwargs):
        new_po_id = self._meta.model.objects.count() + 1
        self.po_no = str(new_po_id)
        super().save(*args, **kwargs)
