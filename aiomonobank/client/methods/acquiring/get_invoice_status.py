from datetime import datetime
from typing import ClassVar, Literal, Optional, List, Any

from pydantic import Field

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.acquiring.shared.cancel_list_item import CancelListItem
from aiomonobank.client.methods.base import Base


class InvoiceStatus(Base):
    status: Literal["created", "processing", "success", "failure", "reversed", "expired"]
    failure_reason: Optional[str] = Field(None, alias="failureReason")
    amount_in_kopecks: int = Field(..., alias="amount")
    ccy: int
    # TODO notify creators of API that this field declared as required, but it's not
    final_amount_in_kopecks: Optional[int] = Field(None, alias="finalAmount")
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    reference: Optional[str] = None
    cancel_list: Optional[List[CancelListItem]] = Field(None, alias="cancelList")

    @property
    def amount(self) -> float:
        return self.amount_in_kopecks / 100

    @property
    def final_amount(self) -> float:
        return self.final_amount_in_kopecks / 100


class GetInvoiceStatus(MonobankAPIMethod[InvoiceStatus]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/invoice/status"
    http_method: ClassVar[str] = "GET"

    invoice_id: str

    def build_request(self, **url_format_kw: Any) -> "Request":
        request = super().build_request(**url_format_kw)
        request.params["invoiceId"] = self.invoice_id
        return request
