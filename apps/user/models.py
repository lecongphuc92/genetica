from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.base.models import TimestampedModel


class User(TimestampedModel, AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    STAFF = 2
    CUSTOMER = 3
    GUEST = 4

    USER_TYPE_CHOICES = (
        (ADMIN, "Admin"),
        (STAFF, "Staff"),
        (CUSTOMER, "Admin"),
        (GUEST, "Guest")
    )

    name = models.CharField(max_length=125)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=15)
    type = models.IntegerField(choices=USER_TYPE_CHOICES, default=CUSTOMER)
