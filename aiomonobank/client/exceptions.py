from json import JSONDecodeError
from typing import Optional, Dict, Any, cast

from aiomonobank.core.session.holder import HTTPResponse
from aiomonobank.utils.compat import json

try:
    from orjson import JSONDecodeError as OrjsonJSONDecodeError
except ImportError:
    OrjsonJSONDecodeError = JSONDecodeError  # noqa  # type: ignore


class MonobankAPIError(Exception):

    def __init__(self, http_response: HTTPResponse, custom_message: Optional[str] = None):
        self._deserialize_cache: Dict[int, Any] = {}
        self._custom_message = custom_message
        self.http_response = http_response

    def json(self) -> Dict[str, Any]:
        return self._deserialize_response()

    def __str__(self) -> str:
        representation = (
            "{message}\n"
            "    * raw response {raw_response}"
        )

        deserialized_response = self._deserialize_response()

        try:
            raw_response: str = json.dumps(deserialized_response, indent=4, ensure_ascii=False)  # type: ignore
        except Exception:  # noqa
            raw_response = self.http_response.body.decode("utf-8")

        error_description = deserialized_response.get("errorDescription", "")

        return representation.format(
            message=self._custom_message or error_description,
            raw_response=raw_response,
        )

    def _deserialize_response(self) -> Dict[str, Any]:
        """
        Deserializing of response many times is practically zero-cost call,
        because response is being cached after the first deserializing
        """
        if self._deserialize_cache.get(id(self.http_response)) is not None:
            return cast(Dict[str, Any], self._deserialize_cache[id(self.http_response)])

        try:
            content: Dict[str, Any] = json.loads(self.http_response.body)
        except (JSONDecodeError, TypeError, OrjsonJSONDecodeError):
            return {}

        self._deserialize_cache[id(self.http_response)] = content
        return content
