from django.db import models

from apps.base.models import TimestampedModel


class ServicePack(TimestampedModel):
    ADULTS = 1
    KIDS = 2
    HEALTH = 3

    TYPE_CHOICES = (
        (ADULTS, "adults"),
        (KIDS, "kids"),
        (HEALTH, "health"),
    )

    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=TYPE_CHOICES, default=ADULTS)
