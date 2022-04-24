import abc
from typing import TypeVar, Generic, Any

from aiomonobank.client.exceptions import MonobankAPIError
from aiomonobank.core.abc.api_method import APIMethod
from aiomonobank.core.session.holder import HTTPResponse

try:
    from orjson import JSONDecodeError as OrjsonDecodeError
except ImportError:
    from json import JSONDecodeError as OrjsonDecodeError

T = TypeVar("T", bound=Any)


class MonobankAPIMethod(APIMethod[T], abc.ABC, Generic[T]):

    @classmethod
    def _validate_response(cls, response: HTTPResponse) -> None:
        if isinstance(response.json(), list):
            return None

        if response.json().get("errorDescription") is not None:
            raise MonobankAPIError(response)
