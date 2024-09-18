from datetime import datetime

from ninja import Schema

from apps.food.schemas import FoodSchema
from apps.process.models import FoodProcess


class ProcessSchema(Schema):
    id: int
    name: str
    food: FoodSchema

    @classmethod
    def prefetched_queryset(cls):
        return FoodProcess.objects.select_related("food")


class CreateProcessRequestSchema(Schema):
    name: str
    food_id: int
