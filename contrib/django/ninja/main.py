from typing import Optional

from ninja import NinjaAPI
from ninja.types import DictStrAny

from contrib.django.ninja.openapi.schema import get_schema, OpenAPISchema


class ContribNinjaAPI(NinjaAPI):
    def get_openapi_schema(
        self,
        *,
        path_prefix: Optional[str] = None,
        path_params: Optional[DictStrAny] = None,
    ) -> OpenAPISchema:
        if path_prefix is None:
            path_prefix = self.get_root_path(path_params or {})
        return get_schema(api=self, path_prefix=path_prefix)
