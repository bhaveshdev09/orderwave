from django.db import models
from backend.models import BaseModel


class Material(BaseModel):
    UNIT_CHOICES = [
        ("kgs", "Kilograms"),
        ("ltrs", "Liters"),
        ("pcs", "Pieces"),
        ("units", "Units"),
    ]

    name = models.CharField(max_length=255, null=False)
    units = models.CharField(max_length=5, choices=UNIT_CHOICES, default="units")
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
