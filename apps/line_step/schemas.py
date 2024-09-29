from typing import Optional

from ninja import Schema

from apps.line.schemas import LineSchema
from apps.line_step.models import FoodProcessLineStep
from apps.step.schemas import StepSchema


class LineStepSchema(Schema):
    id: int
    name: str
    line: LineSchema
    line_id: int
    step: StepSchema
    step_id: int
    step_yield: int
    next_step_id: Optional[int]
    enabled: bool

    @classmethod
    def prefetched_queryset(cls):
        return FoodProcessLineStep.objects.select_related(
            "line__process__food", "line__food", "step__process__food"
        ).prefetch_related("previous_line_steps")


class CreateLineStepRequestSchema(Schema):
    name: str
    line_id: int
    step_id: int
    step_yield: int
    next_step_id: Optional[int]
    enabled: bool


class UpdateLineStepRequestSchema(CreateLineStepRequestSchema): ...
