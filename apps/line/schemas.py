from ninja import Schema

from apps.food.schemas import FoodSchema
from apps.line.models import FoodProcessLine
from apps.process.schemas import ProcessSchema


class LineSchema(Schema):
    id: int
    name: str
    order: int
    bom: int
    process: ProcessSchema
    food: FoodSchema

    @classmethod
    def prefetched_queryset(cls):
        return FoodProcessLine.objects.select_related("food", "process__food")


class CreateLineRequestSchema(Schema):
    name: str
    order: int
    bom: int
    process_id: int
    food_id: int


class UpdateLineRequestSchema(CreateLineRequestSchema): ...
