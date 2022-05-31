from typing import Dict, Any, ClassVar

from pydantic import Field, HttpUrl

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.core.abc.api_method import RuntimeValue
from aiomonobank.core.session.holder import HTTPResponse


class SetWebhook(MonobankAPIMethod[bool]):
    url: ClassVar[str] = "https://api.monobank.ua/personal/webhook"
    http_method: ClassVar[str] = "POST"

    json_payload_schema: ClassVar[Dict[str, Any]] = {
        "webHookUrl": RuntimeValue()
    }

    webhook_url: HttpUrl = Field(..., scheme_path="webHookUrl")

    @classmethod
    def on_json_parse(cls, response: HTTPResponse) -> bool:
        return response.json()["status"] == "ok"
