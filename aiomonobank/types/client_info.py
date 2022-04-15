from typing import List, Optional

from pydantic import Field

from aiomonobank.types.base import Base


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
