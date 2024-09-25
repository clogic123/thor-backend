from apps.core.constants import Constants
from apps.line.models import FoodProcessLine
from apps.line.schemas import CreateLineRequestSchema
from apps.line_step.models import FoodProcessLineStep
from contrib.django.db.transaction import async_atomic


class LineService:
    @async_atomic
    async def create(self, data: CreateLineRequestSchema):
        line = await FoodProcessLine.objects.acreate(**data.dict())
        next_step = None
        for index, name in reversed(Constants.STEP_LIST):
            step = await FoodProcessLineStep.objects.acreate(
                name=name,
                order=index,
                line_id=line.id,
                enabled=True,
                next_step=next_step,
            )
            next_step = step
        return line


line_service = LineService()
