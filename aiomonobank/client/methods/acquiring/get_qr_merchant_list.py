from typing import List, Optional, Literal, ClassVar

from pydantic import Field, parse_obj_as

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.base import Base
from aiomonobank.core.session.holder import HTTPResponse


class QRMerchant(Base):
    short_qr_id: str = Field(..., alias="shortQrId")
    qr_id: Optional[str] = Field(None, alias="qrId")
    amount_type: Optional[Literal["merchant", "client", "fix"]] = Field(None, alias="amountType")
    page_url: Optional[str] = Field(None, alias="pageUrl")


class GetQRMerchantList(MonobankAPIMethod[List[QRMerchant]]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/qr/list"
    http_method: ClassVar[str] = "GET"

    @classmethod
    def on_json_parse(cls, response: HTTPResponse) -> List[QRMerchant]:
        return parse_obj_as(
            cls.__returning_type__, response.json()["list"]
        )

