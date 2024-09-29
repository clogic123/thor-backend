from ninja import Schema

from apps.process.schemas import ProcessSchema
from apps.step.models import FoodProcessStep


class StepSchema(Schema):
    id: int
    name: str
    order: int
    process: ProcessSchema

    @classmethod
    def prefetched_queryset(cls):
        return FoodProcessStep.objects.prefetch_related("process__food")


class CreateStepRequestSchema(Schema):
    name: str
    order: int
    process_id: int


class UpdateStepRequestSchema(CreateStepRequestSchema): ...
