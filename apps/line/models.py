from django.db import models

from contrib.django.models.base import BaseDateTimeModel


# Create your models here.


class FoodProcessLine(BaseDateTimeModel):
    name = models.CharField("name", max_length=128, null=True, blank=True)
    order = models.PositiveSmallIntegerField("order", default=0)
    bom = models.PositiveSmallIntegerField("bom", default=0)
    process = models.ForeignKey(
        "process.FoodProcess",
        on_delete=models.DO_NOTHING,
        related_name="lines",
        db_constraint=False,
    )
    food = models.ForeignKey(
        "food.Food", on_delete=models.DO_NOTHING, db_constraint=False
    )

    class Meta:
        db_table = "food_process_line"
