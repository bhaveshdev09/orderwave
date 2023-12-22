from django.db import models
from backend.models import BaseModel
from django.utils.translation import gettext as _
from django.urls import reverse
from items.models import Section, Category, OperatingHour


class Item(models.Model):
    name = models.CharField(max_length=255, null=False)
    desc = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    operation_hour = models.ForeignKey(OperatingHour, on_delete=models.DO_NOTHING)
    base_price = models.FloatField()
    tax = models.FloatField(default=18, editable=False)

    @property
    def selling_price(self):
        # Your logic for calculating selling price
        return round(self.base_price * 1.18, 1)

    def __str__(self):
        return self.name
