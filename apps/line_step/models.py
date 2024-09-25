from django.db import models

from contrib.django.models.base import BaseDateTimeModel


# Create your models here.


class FoodProcessLineStep(BaseDateTimeModel):
    name = models.CharField("name", max_length=128, null=True, blank=True)
    order = models.PositiveSmallIntegerField("order", default=0)
    line = models.ForeignKey(
        "line.FoodProcessLine",
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name="line_steps",
    )
    step = models.ForeignKey(
        "step.FoodProcessStep",
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name="lien_steps",
    )
    step_yield = models.FloatField("yield", default=100)
    next_step = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name="previous_line_steps",
    )
    enabled = models.BooleanField("enabled", default=True)

    class Meta:
        db_table = "food_process_line_step"
