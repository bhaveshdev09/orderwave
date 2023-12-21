# from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from backend.models import BaseModel


class Customer(BaseModel):
    name = models.CharField(_("customer name"), max_length=255)
    mobile = models.CharField(
        _("customer mobile no"), max_length=15, unique=True, db_index=True
    )
    email = models.EmailField(blank=True)

    class Meta:
        managed = True
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def get_absolute_url(self):
        return reverse("branches:branch-detail", kwargs={"pk": self.pk})
