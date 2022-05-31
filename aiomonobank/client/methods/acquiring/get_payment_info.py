from datetime import datetime
from typing import ClassVar, Optional, Literal, List

from pydantic import Field
from pydantic import PaymentCardNumber

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.acquiring.shared.cancel_list_item import CancelListItem
from aiomonobank.client.methods.base import Base


class PaymentInfo(Base):
    masked_pan: PaymentCardNumber = Field(..., alias="maskedPan")
    approval_code: str = Field(..., alias="approvalCode")
    rrn: str
    amount_in_kopecks: int = Field(..., alias="amount")
    ccy: int
    final_amount_in_kopecks: int = Field(..., alias="finalAmount")
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    terminal: str
    payment_scheme: Literal["full", "bnpl_parts_4", "bnpl_later_30"] = Field(
        ...,
        alias="paymentScheme"
    )
    payment_method: Literal["pan", "apple", "google", "monobank", "monopay"] = Field(
        ...,
        alias="paymentMethod"
    )
    fee: Optional[int] = None
    is_domestic_card: bool = Field(..., alias="domesticCard")
    country: str
    cancel_list: Optional[List[CancelListItem]] = Field(None, alias="cancelList")


class GetPaymentInfo(MonobankAPIMethod[PaymentInfo]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/invoice/payment-info?invoiceId={invoiceId}"
    http_method: ClassVar[str] = "GET"

    invoice_id: str
