from typing import List

from ninja import Router, Query

from apps.step.filters import StepFilterSchema
from apps.step.models import FoodProcessLineStep
from apps.step.schemas import StepSchema, CreateStepRequestSchema

# Create your views here.
router = Router(tags=["steps"])


@router.get("steps", response=List[StepSchema])
async def get_steps(request, filter: StepFilterSchema = Query(...)):
    steps = StepSchema.prefetched_queryset()
    steps = filter.filter(steps)
    steps = [s async for s in steps]
    return steps


@router.get("steps/{step_id}", response=StepSchema)
async def get_step(request, step_id: int):
    step = await StepSchema.prefetched_queryset().aget(step_id)
    return step


@router.put("steps/{step_id}", response=StepSchema)
async def update_step(request, step_id: int, body: CreateStepRequestSchema):
    step = await StepSchema.prefetched_queryset().aget(id=step_id)
    for attr, value in body.dict().items():
        setattr(step, attr, value)

    await step.asave()
    return step


@router.post("steps", response=StepSchema)
async def create_step(request, body: CreateStepRequestSchema):
    step = await FoodProcessLineStep.objects.acreate(**body.dict())
    step = await StepSchema.prefetched_queryset().aget(id=step.id)
    return step


@router.delete("steps/{step_id}")
async def delete_step(request, step_id: int):
    step = await StepSchema.prefetched_queryset().aget(id=step_id)
    await step.adelete()
    return "OK"
