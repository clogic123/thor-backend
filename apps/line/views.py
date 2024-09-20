from typing import List

from django.shortcuts import render
from ninja import Router, Query

from apps.line.filters import LineFilterSchema
from apps.line.models import FoodProcessLine
from apps.line.schemas import (
    LineSchema,
    CreateLineRequestSchema,
    UpdateLineRequestSchema,
)
from apps.line.services import line_service

# Create your views here.
router = Router(tags=["lines"])


@router.get("lines", response=List[LineSchema])
async def get_lines(request, filter: LineFilterSchema = Query(...)):
    lines = LineSchema.prefetched_queryset()
    lines = filter.filter(lines)
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
    line = await LineSchema.prefetched_queryset().aget(id=line_id)
    return line


@router.post("lines", response=LineSchema)
async def create_line(request, body: CreateLineRequestSchema):
    line = await line_service.create(body)
    line = await LineSchema.prefetched_queryset().aget(id=line.id)
    return line


@router.delete("lines/{int:line_id}")
async def delete_line(request, line_id: int):
    line = await LineSchema.prefetched_queryset().aget(id=line_id)
    await line.adelete()
    return "OK"
