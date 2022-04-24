import functools
from datetime import datetime
from typing import Optional, Any

from pydantic import Field, BaseConfig

from aiomonobank.types.arbitrary.currency import Currency
from aiomonobank.types.arbitrary.currency_data import parse_currency_by_code
from aiomonobank.types.base import Base
from aiomonobank.utils.dates import convert_to_unix_time, parse_unix_time


class ExchangeRate(Base):
    unix_date: int = Field(..., alias="date")
    currency_code_a: int = Field(..., alias="currencyCodeA")
    currency_code_b: int = Field(..., alias="currencyCodeB")
    rate_sell: Optional[float] = Field(None, alias="rateSell")
    rate_buy: Optional[float] = Field(None, alias="rateBuy")
    rate_cross: Optional[float] = Field(None, alias="rateCross")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, ExchangeRate):
            return False

        return (
                self.currency_code_a == other.currency_code_a
                and
                self.currency_code_b == self.currency_code_b
                and
                self.unix_date == other.unix_date
        )

    def __hash__(self) -> int:
        return hash((self.currency_code_a, self.currency_code_b, self.unix_date))

    class Config(BaseConfig):
        json_encoders = {
            datetime: lambda dt: convert_to_unix_time(dt)
        }

    @property
    @functools.cache
    def currency_a(self) -> Currency:
        return parse_currency_by_code(self.currency_code_a)

    @property
    @functools.cache
    def currency_b(self) -> Currency:
        return parse_currency_by_code(self.currency_code_b)

    @property
    @functools.cache
    def date_as_datetime(self) -> datetime:
        return parse_unix_time(self.unix_date)
