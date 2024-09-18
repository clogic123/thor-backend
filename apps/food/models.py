from django.db import models

from contrib.django.models.base import BaseDateTimeModel


# Create your models here.


class Food(BaseDateTimeModel):
    name = models.CharField("name", max_length=128, null=True, blank=True)
    code = models.CharField("code", max_length=128, null=True, blank=True)

    class Meta:
        db_table = "food"
