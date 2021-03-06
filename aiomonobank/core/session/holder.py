from __future__ import annotations

import abc
import sys
import traceback
import warnings
from dataclasses import dataclass
from types import TracebackType
from typing import Any, Generic, Optional, Type, TypeVar, cast, Mapping, Dict

import aiohttp
from aiohttp import ClientResponse

from aiomonobank.utils.compat import json
from aiomonobank.utils.helpers import get_running_loop

_SessionType = TypeVar("_SessionType", bound=Any)
_SessionHolderType = TypeVar("_SessionHolderType", bound="AbstractSessionHolder[Any]")


@dataclass
class HTTPResponse:
    """
    Wrapper over different third-party HTTP client responses.
    """
    status_code: int
    body: bytes
    headers: Mapping[str, Any]
    content_type: str
    _real_response: Any

    def json(self) -> Any:
        return cast(Dict[str, Any], json.loads(self.body))

    def __getattr__(self, item: str) -> Any:
        return getattr(self._real_response, item)

    @property
    def has_successful_status_code(self) -> bool:
        """Returns ``True`` if ``status`` is less than ``400``, ``False`` if not.

        This is **not** a check for ``200 OK`` but a check that the response
        status is under 400.
        """
        return 400 > self.status_code


class AbstractSessionHolder(abc.ABC, Generic[_SessionType]):
    """
    Manages the lifecycle of the session (s) and allows spoofing
    library for requests, for example from aiohttp to httpx without any problem.
    Holder is lazy and allocates in his own state
    session on first call, not on instantiation.
    """

    def __init__(self, **kwargs: Any) -> None:
        self._session: Optional[_SessionType] = None
        self._session_kwargs = kwargs

    @abc.abstractmethod
    async def convert_third_party_lib_response_to_http_response(
            self, response: Any
    ) -> HTTPResponse:
        raise NotImplementedError

    def update_session_kwargs(self, **kwargs: Any) -> None:
        self._session_kwargs.update(kwargs)

    async def __aenter__(self: AbstractSessionHolder[_SessionType]) -> _SessionType:
        self._session = await self.get_session()
        return self._session

    @abc.abstractmethod
    async def get_session(self) -> _SessionType:
        raise NotImplementedError

    async def __aexit__(
            self: AbstractSessionHolder[_SessionType],
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> None:
        await self.close()

    @abc.abstractmethod
    async def close(self) -> None:
        raise NotImplementedError


class AiohttpSessionHolder(AbstractSessionHolder[aiohttp.ClientSession]):
    _closed = None  # Serves as an uninitialized flag for __del__
    _source_traceback = None  # type: Optional[traceback.StackSummary]

    def __init__(self, **kwargs: Any):
        AbstractSessionHolder.__init__(self, **kwargs)
        self._loop = kwargs.get("loop") or get_running_loop()

        if self._loop.get_debug():
            self._source_traceback = traceback.extract_stack(sys._getframe(1))
        self._closed = False

    def __del__(self, _warnings=warnings):
        if self._closed is False:
            _warnings.warn(
                f"Unclosed AiohttpSessionHolder {self!r}, probably you need to "
                f"close your client after usage or use it as a context manager",
                ResourceWarning,
                source=self
            )
            context = {
                'session_holder': self,
                'message': f"Unclosed AiohttpSessionHolder {self!r}, probably you need to "
                           f"close your client after usage or use it as a context manager"
            }
            if self._source_traceback is not None:
                context['source_traceback'] = self._source_traceback
            self._loop.call_exception_handler(context)

    async def close(self) -> None:
        if self._session_in_working_order():
            await self._session.close()

        self._closed = True

    async def convert_third_party_lib_response_to_http_response(
            self, response: ClientResponse
    ) -> HTTPResponse:
        return HTTPResponse(
            status_code=response.status,
            body=await response.read(),
            headers=response.headers,
            content_type=response.content_type,
            _real_response=response
        )

    async def get_session(self) -> _SessionType:
        if self._session_in_working_order():
            return self._session
        return await self._instantiate_new_session()

    def _session_in_working_order(self) -> bool:
        return self._session is not None and self._session.closed is False

    async def _instantiate_new_session(self) -> _SessionType:
        self._session: _SessionType = cast(
            _SessionType, aiohttp.ClientSession(**self._session_kwargs)
        )
        return self._session
