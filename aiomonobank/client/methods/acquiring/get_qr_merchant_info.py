from typing import ClassVar, Optional

from pydantic import Field

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.base import Base


class QRMerchantInfo(Base):
    short_qr_id: str = Field(..., alias="shortQrId")
    invoice_id: Optional[str] = Field(None, alias="invoiceId")
    amount_in_kopecks: Optional[int] = Field(None, alias="amount")
    ccy: Optional[int] = None


class GetQRMerchantInfo(MonobankAPIMethod[QRMerchantInfo]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/qr/details"
    http_method: ClassVar[str] = "GET"

    qr_id: str = Field(..., alias="qrId")
