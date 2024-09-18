from typing import Any, List

from django.db.models import QuerySet
from ninja import Schema
from ninja.conf import settings
from ninja.pagination import AsyncPaginationBase
from pydantic import Field


class CursorPagination(AsyncPaginationBase):
    class Input(Schema):
        last_id: int = Field(0, ge=0)

    class Output(Schema):
        items: List[Any]

    def __init__(self, size: int = settings.PAGINATION_PER_PAGE, **kwargs: Any) -> None:
        self.size = size
        super().__init__(**kwargs)

    def paginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> Any:
        queryset = queryset.filter(id__gt=pagination.last_id)
        return {
            "items": queryset[: self.size],
        }  # noqa: E203

    async def apaginate_queryset(
        self,
        queryset: QuerySet,
        pagination: Input,
        **params: Any,
    ) -> Any:
        queryset = queryset.filter(id__gt=pagination.last_id)
        return {
            "items": [q async for q in queryset[: self.size]],
        }  # noqa: E203
