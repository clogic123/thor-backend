from typing import Optional

from ninja import Schema

from apps.step.models import FoodProcessLineStep


class StepSchema(Schema):
    id: int
    name: str
    order: int
    next_step_id: Optional[int]

    @classmethod
    def prefetched_queryset(cls):
        return FoodProcessLineStep.objects.all()


class CreateStepRequestSchema(Schema):
    name: str
    order: int
    next_step_id: Optional[int]


class UpdateStepRequestSchema(CreateStepRequestSchema): ...
