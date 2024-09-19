from typing import List

from django.shortcuts import render
from ninja import Router

from apps.line.models import FoodProcessLine
from apps.line.schemas import (
    LineSchema,
    CreateLineRequestSchema,
    UpdateLineRequestSchema,
)

# Create your views here.
router = Router(tags=["lines"])


@router.get("lines", response=List[LineSchema])
async def get_lines(request):
    lines = LineSchema.prefetched_queryset()
    lines = [l async for l in lines]
    return lines


@router.get("lines/{int:line_id}", response=LineSchema)
async def get_line(request, line_id: int):
    line = await LineSchema.prefetched_queryset().aget(id=line_id)
    return line


@router.put("lines/{int:line_id}", response=LineSchema)
async def update_line(request, line_id: int, body: UpdateLineRequestSchema):
    line = await LineSchema.prefetched_queryset().aget(id=line_id)
    for attr, value in body.dict().items():
        setattr(line, attr, value)

    await line.asave()
    return line


@router.post("lines", response=LineSchema)
async def create_line(request, body: CreateLineRequestSchema):
    line = await FoodProcessLine.objects.acreate(**body.dict())
    line = await LineSchema.prefetched_queryset().aget(id=line.id)
    return line


@router.delete("lines/{int:line_id}")
async def delete_line(request, line_id: int):
    line = await LineSchema.prefetched_queryset().aget(id=line_id)
    await line.adelete()
    return "OK"
