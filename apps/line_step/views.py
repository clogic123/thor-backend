from typing import List

from ninja import Router, Query

from apps.food.models import Food
from apps.line_step.filters import StepFilterSchema
from apps.line_step.models import FoodProcessLineStep
from apps.line_step.schemas import LineStepSchema, CreateLineStepRequestSchema
from contrib.django.db.transaction import async_atomic
from contrib.django.ninja.errors import BadRequestError, ErrorSchema

# Create your views here.
router = Router(tags=["line steps"])


@router.get("line-steps", response=List[LineStepSchema])
async def get_line_steps(request, filter: StepFilterSchema = Query(...)):
    steps = LineStepSchema.prefetched_queryset()
    steps = filter.filter(steps)
    steps = [s async for s in steps]
    return steps


@router.get("line-steps/{step_id}", response=LineStepSchema)
async def get_line_step(request, step_id: int):
    step = await LineStepSchema.prefetched_queryset().aget(id=step_id)
    return step


@router.put("line-steps/{step_id}", response={200: LineStepSchema, 400: ErrorSchema})
async def update_line_step(request, step_id: int, body: CreateLineStepRequestSchema):
    step: FoodProcessLineStep = await LineStepSchema.prefetched_queryset().aget(
        id=step_id
    )
    next_step: FoodProcessLineStep = await LineStepSchema.prefetched_queryset().aget(
        id=body.next_step_id
    )

    if body.enabled == False:
        for previous in step.previous_line_steps.all():
            previous.next_step_id = None
            await previous.asave()

    if step.line.process != next_step.line.process:
        raise BadRequestError("같은 프로세스가 아닌 스텝은 연결할 수 없습니다.")

    for attr, value in body.dict().items():
        setattr(step, attr, value)

    await step.asave()
    step = await LineStepSchema.prefetched_queryset().aget(id=step_id)
    return step


@router.post("line-steps", response=LineStepSchema)
async def create_line_step(request, body: CreateLineStepRequestSchema):
    line_step = await FoodProcessLineStep.objects.acreate(**body.dict())
    line_step = await LineStepSchema.prefetched_queryset().aget(id=line_step.id)
    return line_step


@router.delete("line-steps/{step_id}")
async def delete_line_step(request, step_id: int):
    step = await LineStepSchema.prefetched_queryset().aget(id=step_id)
    await step.adelete()
    return "OK"
