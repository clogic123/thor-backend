from apps.core.constants import Constants
from apps.line.models import FoodProcessLine
from apps.line.schemas import CreateLineRequestSchema
from apps.line_step.models import FoodProcessLineStep
from contrib.django.db.transaction import async_atomic


class LineService:
    @async_atomic
    async def create(self, data: CreateLineRequestSchema):
        line = await FoodProcessLine.objects.acreate(**data.dict())
        return line


line_service = LineService()
