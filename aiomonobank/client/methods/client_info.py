from typing import ClassVar

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.types.client_info import ClientInfo


class GetClientInfo(MonobankAPIMethod[ClientInfo]):
    url: ClassVar[str] = "https://api.monobank.ua/personal/client-info"
    http_method: ClassVar[str] = "GET"

