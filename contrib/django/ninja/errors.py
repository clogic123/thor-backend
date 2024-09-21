from ninja import Schema
from ninja.errors import HttpError


class ErrorSchema(Schema):
    detail: str


class BaseHttpError(HttpError):
    def __init__(self, message=""):
        self.message = message


class BadRequestError(BaseHttpError):
    status_code = 400
    message = "Bad request"


class NotFoundError(BaseHttpError):
    status_code = 404
    message = "Not found"


class UnauthorizedError(BaseHttpError):
    status_code = 401
