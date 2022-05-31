from datetime import datetime
from typing import ClassVar, Union, List, Optional, Literal

from pydantic import Field, validator, HttpUrl

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.base import Base
from aiomonobank.core.abc.api_method import RuntimeValue
from aiomonobank.utils.dates import convert_to_unix_time


class Invoice(Base):
    invoice_id: str = Field(..., alias="invoiceId")
    page_url: str = Field(..., alias="pageUrl")


class BasketPosition(Base):
    name: str
    qty: int
    sum: Union[float, int]
    icon: str
    unit: str


class BasketOrder(Base):
    __root__: List[BasketPosition]


class MerchantPaymentInfo(Base):
    reference: str
    destination: str
    basket_order: BasketOrder


class CreateInvoice(MonobankAPIMethod[Invoice]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/invoice/create"
    http_method: ClassVar[str] = "POST"

    json_payload_schema: ClassVar = {
        "amount": RuntimeValue(),
        "ccy": RuntimeValue(mandatory=False),
        "merchantPaymInfo": RuntimeValue(mandatory=False),
        "redirectUrl": RuntimeValue(mandatory=False),
        "webHookUrl": RuntimeValue(mandatory=False),
        "validity": RuntimeValue(mandatory=False),
        "paymentType": RuntimeValue(mandatory=False),
        "qrId": RuntimeValue(mandatory=False),
    }

    amount: Union[int, float, str] = Field(..., scheme_path="amount")
    ccy: Optional[int] = None
    merchant_payment_info: Optional[MerchantPaymentInfo] = Field(None, scheme_path="merchantPaymInfo")
    redirect_url: Optional[HttpUrl] = Field(None, scheme_path="redirectUrl")
    webhook_url: Optional[HttpUrl] = Field(None, scheme_path="webHookUrl")
    validity: Optional[Union[float, int, datetime]] = Field(None, scheme_path="validity")
    payment_type: Union[Literal["debit", "hold"], None] = Field(None, scheme_path="paymentType")
    qr_id: Optional[str] = Field(None, scheme_path="qrId")

    @validator("amount")
    def convert_amount_to_kopecks(cls, v: Union[int, float, str]) -> int:
        if isinstance(v, str):
            v = float(v)
        return v * 100

    @validator("validity")
    def convert_validity_to_unix_time(cls, valid_until: Union[float, int, datetime]) -> float:
        if isinstance(valid_until, datetime):
            return convert_to_unix_time(valid_until)

        return valid_until
