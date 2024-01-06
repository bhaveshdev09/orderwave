from django.db import models
from django.utils.translation import gettext as _
from backend.models import BaseModel
from django.utils.text import slugify
from django.urls import reverse

class Aggregator(BaseModel):
    name = models.CharField(_("Aggregator Name"), max_length=50)
    slug = models.SlugField(_("slug"), max_length=255, unique=True, editable=False)
    is_deleted = models.BooleanField(_("deleted"), default=False)

    class Meta:
        managed = True
        verbose_name = "Aggregator"
        verbose_name_plural = "Aggregators"

    def get_absolute_url(self):
        return reverse("aggregators:aggregator-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        # auto-generate slug based on the first two characters of the name
        self.name = self.name.lower()
        self.slug = slugify(self.name[:2])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name