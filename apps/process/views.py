from typing import List

from django.shortcuts import render
from ninja import Router

from apps.process.models import FoodProcess
from apps.process.schemas import (
    ProcessSchema,
    CreateProcessRequestSchema,
    UpdateProcessRequestSchema,
)

# Create your views here.
router = Router(tags=["processes"])


@router.get("processes", response=List[ProcessSchema])
async def get_processes(request):
    processes = ProcessSchema.prefetched_queryset()
    processes = [p async for p in processes]
    return processes


@router.get("processes/{int:process_id}", response=ProcessSchema)
async def get_process(request, process_id: int):
    process = await ProcessSchema.prefetched_queryset().aget(id=process_id)
    return process


@router.put("processes/{int:process_id}", response=ProcessSchema)
async def update_process(request, process_id: int, body: UpdateProcessRequestSchema):
    process = await ProcessSchema.prefetched_queryset().aget(id=process_id)
    for attr, value in body.dict().items():
        setattr(process, attr, value)

    await process.asave()
    return process


@router.post("processes", response=ProcessSchema)
async def create_process(request, body: CreateProcessRequestSchema):
    process = await FoodProcess.objects.acreate(**body.dict())
    process = await ProcessSchema.prefetched_queryset().aget(id=process.id)
    return process
