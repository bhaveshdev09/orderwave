from django.db import models
from backend.models import BaseModel


class Material(BaseModel):
    # Unit Choices
    UNIT_CHOICE_KILOGRAMS = "kgs"
    UNIT_CHOICE_LITERS = "ltrs"
    UNIT_CHOICE_PIECES = "pcs"
    UNIT_CHOICE_UNITS = "units"

    UNIT_CHOICES = [
        (UNIT_CHOICE_KILOGRAMS, "Kilograms"),
        (UNIT_CHOICE_LITERS, "Liters"),
        (UNIT_CHOICE_PIECES, "Pieces"),
        (UNIT_CHOICE_UNITS, "Units"),
    ]

    name = models.CharField(max_length=255, null=False, unique=True)
    units = models.CharField(max_length=10, choices=UNIT_CHOICES, default="units")
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
