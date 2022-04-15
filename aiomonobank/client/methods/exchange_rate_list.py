from typing import ClassVar, List

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.types.exchange_rate import ExchangeRate


class GetExchangeRates(MonobankAPIMethod[List[ExchangeRate]]):
    url: ClassVar[str] = "https://api.monobank.ua/bank/currency"
    http_method: ClassVar[str] = "GET"
