from django.db import models

from contrib.django.models.base import BaseDateTimeModel


class FoodProcess(BaseDateTimeModel):

    name = models.CharField("name", max_length=128, null=True, blank=True)
    food = models.ForeignKey(
        "food.Food",
        on_delete=models.DO_NOTHING,
        related_name="processes",
        db_constraint=False,
    )

    class Meta:
        db_table = "food_process"
