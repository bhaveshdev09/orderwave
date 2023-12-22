from django.db import models
from backend.models import BaseModel
from django.utils.translation import gettext as _
from django.urls import reverse


class Category(BaseModel):
    title = models.CharField(max_length=255, null=False)
    is_deleted = models.BooleanField(_("deleted"), default=False)

    class Meta:
        managed = True
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("items:category-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
