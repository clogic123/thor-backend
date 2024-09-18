import json
from typing import cast

import humps
from django.http import HttpRequest
from ninja.parser import Parser
from ninja.types import DictStrAny


class CamelParser(Parser):
    def parse_body(self, request: HttpRequest) -> DictStrAny:
        return cast(DictStrAny, humps.decamelize(json.loads(request.body)))
