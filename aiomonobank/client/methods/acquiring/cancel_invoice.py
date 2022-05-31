from datetime import datetime
from typing import Literal, Optional, ClassVar

from pydantic import Field

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.base import Base
from aiomonobank.core.abc.api_method import RuntimeValue


class CancelInvoiceStatus(Base):
    status: Literal["processing", "success", "failure"]
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")


class CancelInvoice(MonobankAPIMethod[CancelInvoiceStatus]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/invoice/cancel"
    http_method: ClassVar[str] = "POST"

    json_payload_schema = {
        "invoiceId": RuntimeValue(),
        "amount": RuntimeValue(mandatory=False),
    }

    invoice_id: str
    amount: Optional[int] = None
