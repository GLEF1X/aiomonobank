from typing import ClassVar, Optional, List

from pydantic import Field

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.base import Base


class Account(Base):
    id: str
    balance: int
    creditLimit: int
    type: str
    currency_code: str = Field(..., alias="currencyCode")
    cashback_type: str = Field(..., alias="cashbackType")


class ClientInfo(Base):
    id: Optional[str] = None
    name: str
    webhook_url: str = Field(None, alias="webHookUrl")
    accounts: List[Account]


class GetClientInfo(MonobankAPIMethod[ClientInfo]):
    url: ClassVar[str] = "https://api.monobank.ua/personal/client-info"
    http_method: ClassVar[str] = "GET"
