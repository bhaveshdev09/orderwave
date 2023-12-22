from django.db import models
from backend.models import BaseModel
from django.urls import reverse
from django.utils.translation import gettext as _


class OperatingHour(BaseModel):
    class Tag(models.TextChoices):
        ALL_DAY = "AD", _("All Day")
        BREAKFAST = "BR", _("Breakfast")
        LUNCH = "LU", _("Lunch")
        DINNER = "DN", _("Dinner")
        SNACKS = "SN", _("Snacks")
        # CUSTOM = "CM", _("Custom")   # TODO:future Use Case

    from_time = models.TimeField()
    to_time = models.TimeField()
    tags = models.CharField(max_length=50, choices=Tag.choices, default=Tag.ALL_DAY)
    title = models.CharField(max_length=255, null=False)

    class Meta:
        managed = True
        verbose_name = "operating_hour"
        verbose_name_plural = "operating_hours"

    def get_absolute_url(self):
        return reverse("items:operating-hour-detail", kwargs={"pk": self.pk})
