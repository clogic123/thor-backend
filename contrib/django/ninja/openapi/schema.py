import humps
from ninja.openapi.schema import OpenAPISchema as BaseOpenAPISchema
from ninja.types import DictStrAny


def get_schema(api: "NinjaAPI", path_prefix: str = "") -> "OpenAPISchema":
    openapi = OpenAPISchema(api, path_prefix)
    return openapi


class OpenAPISchema(BaseOpenAPISchema):

    def get_paths(self) -> DictStrAny:
        result = super().get_paths()
        for v in result.values():
            for path in v.values():
                for param in path["parameters"]:
                    if param["in"] == "query":
                        param["name"] = humps.camelize(param["name"])
        return result

    def get_components(self) -> DictStrAny:
        result = super().get_components()
        for k, v in result["schemas"].items():
            v["properties"] = humps.camelize(v["properties"])
        return result
