# users/models.py
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, mobile_no, password="abcd@123", **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, mobile_no=mobile_no, **extra_fields)
        # set a base password for all users
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_no, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, mobile_no, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    branch = models.ForeignKey(
        "branches.Branch", on_delete=models.DO_NOTHING, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile_no"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
