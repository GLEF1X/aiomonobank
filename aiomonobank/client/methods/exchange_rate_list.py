from datetime import datetime
from typing import ClassVar, List, Optional, Any

from pydantic import Field, BaseConfig

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.client.methods.arbitrary.currency import Currency
from aiomonobank.client.methods.arbitrary.currency_data import parse_currency_by_code
from aiomonobank.client.methods.base import Base
from aiomonobank.utils.dates import convert_to_unix_time, parse_unix_time


class ExchangeRate(Base):
    unix_date: int = Field(..., alias="date")
    currency_code_a: int = Field(..., alias="currencyCodeA")
    currency_code_b: int = Field(..., alias="currencyCodeB")
    rate_sell: Optional[float] = Field(None, alias="rateSell")
    rate_buy: Optional[float] = Field(None, alias="rateBuy")
    rate_cross: Optional[float] = Field(None, alias="rateCross")

    def __eq__(self, other: Any) -> bool:
        return (
            (
                self.currency_code_a == other.currency_code_a
                and self.currency_code_b == self.currency_code_b
                and self.unix_date == other.unix_date
            )
            if isinstance(other, ExchangeRate)
            else False
        )

    def __hash__(self) -> int:
        return hash((self.currency_code_a, self.currency_code_b, self.unix_date))

    class Config(BaseConfig):
        json_encoders = {
            datetime: lambda dt: convert_to_unix_time(dt)
        }

    @property
    def currency_a(self) -> Currency:
        return parse_currency_by_code(self.currency_code_a)

    @property
    def currency_b(self) -> Currency:
        return parse_currency_by_code(self.currency_code_b)

    @property
    def date_as_datetime(self) -> datetime:
        return parse_unix_time(self.unix_date)


class GetExchangeRates(MonobankAPIMethod[List[ExchangeRate]]):
    url: ClassVar[str] = "https://api.monobank.ua/bank/currency"
    http_method: ClassVar[str] = "GET"
