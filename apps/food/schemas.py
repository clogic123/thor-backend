from ninja import Schema


class FoodSchema(Schema):
    id: int
    name: str
    code: str


class CreateFoodRequestSchema(Schema):
    name: str
    code: str


class UpdateFoodRequestSchema(CreateFoodRequestSchema): ...
