from ninja import FilterSchema


class LineFilterSchema(FilterSchema):
    process_id: int = None
