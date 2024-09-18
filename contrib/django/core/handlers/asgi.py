from functools import cached_property

import humps
from django.core.handlers.asgi import (
    ASGIHandler as BaseASGIHandler,
    ASGIRequest as BaseASGIRequest,
)
from django.http import QueryDict
from django.utils.datastructures import MultiValueDict


class ASGIRequest(BaseASGIRequest):

    @cached_property
    def GET(self):
        obj = QueryDict(self.META["QUERY_STRING"], mutable=True)
        data = MultiValueDict()
        for key in obj.keys():
            for val in obj.getlist(key):
                data.appendlist(humps.decamelize(key), val)

        return data


class ASGIHandler(BaseASGIHandler):
    request_class = ASGIRequest
