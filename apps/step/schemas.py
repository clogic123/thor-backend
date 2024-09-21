from typing import Optional

from ninja import Schema

from apps.line.schemas import LineSchema
from apps.step.models import FoodProcessLineStep


class StepSchema(Schema):
    id: int
    name: str
    order: int
    line: LineSchema
    line_id: int
    step_yield: int
    next_step_id: Optional[int]
    enabled: bool

    @classmethod
    def prefetched_queryset(cls):
        return FoodProcessLineStep.objects.select_related(
            "line__process__food", "line__food"
        ).all()


class CreateStepRequestSchema(Schema):
    name: str
    order: int
    line_id: int
    step_yield: int
    next_step_id: Optional[int]
    enabled: bool


class UpdateStepRequestSchema(CreateStepRequestSchema): ...
