from django.db import models
from backend.models import BaseModel
from django.utils.translation import gettext as _
from django.urls import reverse
from items.models import Section, Category, OperatingHour


class Item(BaseModel):
    name = models.CharField(max_length=255, null=False)
    desc = models.TextField(blank=True, default="")
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    operation_hour = models.ManyToManyField(OperatingHour)
    base_price = models.FloatField()
    tax = models.FloatField(default=5, blank=True)
    is_active = models.BooleanField(_("active"), default=True)

    @property
    def selling_price(self):
        # Your logic for calculating selling price
        return round(self.base_price * (self.tax * 0.01 + 1), 1)

    @property
    def is_available(self):
        pass

    @classmethod
    def get_available_items(cls):
        current_operating_hours = OperatingHour.get_current_operating_hour()
        return cls._default_manager.filter(operation_hour__in=current_operating_hours)

    def __str__(self):
        return self.name
