from typing import List

from ninja import Router

from apps.step.models import FoodProcessLineStep
from apps.step.schemas import StepSchema, CreateStepRequestSchema

# Create your views here.
router = Router(tags=["steps"])


@router.get("steps", response=List[StepSchema])
async def get_steps(request):
    steps = StepSchema.prefetched_queryset()
    steps = [s async for s in steps]
    return steps


@router.get("steps/{step_id}", response=StepSchema)
async def get_step(request, step_id: int):
    step = await StepSchema.prefetched_queryset().aget(step_id)
    return step


@router.post("steps", response=StepSchema)
async def create_step(request, body: CreateStepRequestSchema):
    step = await FoodProcessLineStep.objects.acreate(**body.dict())
    step = await StepSchema.prefetched_queryset().aget(id=step.id)
    return step
