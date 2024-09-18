import humps
from ninja.renderers import BaseRenderer, JSONRenderer


class CamelCaseRenderer(JSONRenderer):
    def render(self, request, data, *, response_status):
        return super().render(request, humps.camelize(data), response_status=response_status)