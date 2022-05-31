from datetime import datetime
from typing import ClassVar, Optional, Literal, List

from pydantic import Field

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.acquiring.shared.cancel_list_item import CancelListItem
from aiomonobank.client.methods.base import Base


class MerchantDetails(Base):
    merchant_id: str = Field(..., alias="merchantId")
    merchant_name: str = Field(..., alias="merchantName")


class GetMerchantDetails(MonobankAPIMethod[MerchantDetails]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/details"
    http_method: ClassVar[str] = "GET"
