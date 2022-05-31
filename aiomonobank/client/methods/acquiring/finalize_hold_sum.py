from typing import ClassVar, Optional

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.core.session.holder import HTTPResponse


class FinalizeHoldSum(MonobankAPIMethod[str]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/invoice/finalize"
    http_method: ClassVar[str] = "POST"

    invoice_id: str
    amount: Optional[int] = None

    @classmethod
    def on_json_parse(cls, response: HTTPResponse) -> str:
        return response.json()["status"]
