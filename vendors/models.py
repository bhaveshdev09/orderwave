from django.db import models
from backend.models import BaseModel


class Vendor(BaseModel):
    name = models.CharField(max_length=255, null=False)
    addr = models.TextField()
    mobile = models.CharField(max_length=15, null=False, unique=True)
    email = models.CharField(
        max_length=30, blank=True
    )  # Problem facing with email field

    class Meta:
        managed = True
        verbose_name = "vendor"
        verbose_name_plural = "vendors"

    def __str__(self):
        return self.name
