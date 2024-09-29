from ninja import FilterSchema


class StepFilterSchema(FilterSchema):
    process_id: int = None
