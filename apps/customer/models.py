from django.db import models

from apps.base.models import TimestampedModel
from apps.servicepack.models import ServicePack
from apps.user.models import User


class Customer(TimestampedModel):
    name = models.CharField(max_length=125)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GenProfile(TimestampedModel):
    name = models.CharField(max_length=125)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service_pack = models.ForeignKey(ServicePack, on_delete=models.CASCADE)


class TestSample(TimestampedModel):
    COLLECT = 1
    VALIDATE = 2
    PROCESSING = 3
    DONE = 4
    FAIL = 5
    RE_COLLECT = 6

    STATUS_CHOICES = (
        (COLLECT, "Collect"),
        (VALIDATE, "Validate"),
        (PROCESSING, "Processing"),
        (DONE, "Done "),
        (FAIL, "Fail"),
        (RE_COLLECT, "Re-Collect")
    )

    gen_profile = models.ForeignKey(GenProfile, on_delete=models.CASCADE)
    staff_collect = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_validate = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_process = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=COLLECT)



