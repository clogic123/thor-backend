from ninja import FilterSchema


class StepFilterSchema(FilterSchema):
    line_id: int = None
