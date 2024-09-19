from typing import List

from django.shortcuts import render
from ninja import Router

from apps.food.models import Food
from apps.food.schemas import (
    FoodSchema,
    CreateFoodRequestSchema,
    UpdateFoodRequestSchema,
)

# Create your views here.


router = Router(tags=["foods"])


@router.get("foods", response=List[FoodSchema])
async def get_foods(request):
    foods = Food.objects.all()
    foods = [f async for f in foods]
    return foods


@router.get("foods/{int:food_id}", response=FoodSchema)
async def get_line(request, food_id: int):
    food = await Food.objects.aget(id=food_id)
    return food


@router.put("foods/{int:food_id}", response=FoodSchema)
async def update_food(request, food_id: int, body: UpdateFoodRequestSchema):
    food = await Food.objects.aget(id=food_id)
    for attr, value in body.dict().items():
        setattr(food, attr, value)
    await food.asave()
    return food


@router.post("foods", response=FoodSchema)
async def create_food(request, body: CreateFoodRequestSchema):
    food = await Food.objects.acreate(**body.dict())
    return food
