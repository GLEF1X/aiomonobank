from typing import Dict, Any, ClassVar

from pydantic import Field

from aiomonobank.client.base import MonobankAPIMethod


class SetWebhook(MonobankAPIMethod[Dict[str, Any]]):
    url: ClassVar[str] = "https://api.monobank.ua/personal/webhook"
    http_method: ClassVar[str] = "POST"

    webhook_url: str = Field(..., alias="webHookUrl")
