from typing import List

from ninja import Router, Query

from apps.food.models import Food
from apps.step.filters import StepFilterSchema
from apps.step.models import FoodProcessLineStep
from apps.step.schemas import StepSchema, CreateStepRequestSchema
from contrib.django.ninja.errors import BadRequestError, ErrorSchema

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
    step = await StepSchema.prefetched_queryset().aget(id=step_id)
    return step


@router.put("steps/{step_id}", response={200: StepSchema, 400: ErrorSchema})
async def update_step(request, step_id: int, body: CreateStepRequestSchema):
    step: FoodProcessLineStep = await StepSchema.prefetched_queryset().aget(id=step_id)
    next_step: FoodProcessLineStep = await StepSchema.prefetched_queryset().aget(
        id=body.next_step_id
    )

    if step.line.process != next_step.line.process:
        raise BadRequestError("같은 프로세스가 아닌 스텝은 연결할 수 없습니다.")

    if next_step.enabled == False:
        raise BadRequestError(
            "활성화되지 않은 스텝을 다음 스텝으로 지정할 수 없습니다."
        )

    for attr, value in body.dict().items():
        setattr(step, attr, value)

    await step.asave()
    step = await StepSchema.prefetched_queryset().aget(id=step_id)
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
