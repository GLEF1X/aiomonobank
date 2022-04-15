from typing import Optional

from pydantic import Field

from aiomonobank.types.base import Base


class ExchangeRate(Base):
    date: int
    currency_code_a: int = Field(..., alias="currencyCodeA")
    currency_code_b: int = Field(..., alias="currencyCodeB")
    rate_sell: Optional[float] = Field(None, alias="rateSell")
    rate_buy: Optional[float] = Field(None, alias="rateBuy")
    rate_cross: Optional[float] = Field(None, alias="rateCross")
