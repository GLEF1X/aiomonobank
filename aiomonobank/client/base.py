import abc
import types
from http import HTTPStatus
from json import JSONDecodeError
from typing import TypeVar, Generic, Any, Sequence, ClassVar, cast

from aiomonobank.client.exceptions import MonobankAPIError
from aiomonobank.core.abc.api_method import APIMethod, ReturningType, _sentinel
from aiomonobank.core.session.holder import HTTPResponse

try:
    from orjson import JSONDecodeError as OrjsonDecodeError
except ImportError:
    from json import JSONDecodeError as OrjsonDecodeError

T = TypeVar("T", bound=Any)


class MonobankAPIMethod(APIMethod[T], abc.ABC, Generic[T]):

    @classmethod
    def parse_http_response(cls, response: HTTPResponse) -> ReturningType:
        try:
            json_response = response.json()
        except (JSONDecodeError, TypeError, OrjsonDecodeError):
            json_response = {}

        try:
            error_description = json_response.get("errorDescription")
        except AttributeError:  # if json is list of objects
            error_description = None

        if error_description:
            raise MonobankAPIError(response)

        # micro optimization that helps to avoid json re-deserialization
        response.json = types.MethodType(lambda self: json_response, response)  # type: ignore

        manually_parsed_json = cls.on_json_parse(response)
        if manually_parsed_json is not _sentinel:
            return cast(ReturningType, manually_parsed_json)

        return super().parse_http_response(response)
