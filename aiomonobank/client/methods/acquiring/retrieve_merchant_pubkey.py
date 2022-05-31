import base64
from typing import ClassVar

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.core.session.holder import HTTPResponse


class Base64Encodedx509Pubkey(str):
    @property
    def decoded_payload_of_pubkey(self) -> bytes:
        return base64.b64decode(self)


class RetrieveMerchantPubkey(MonobankAPIMethod[str]):
    url: ClassVar[str] = "https://api.monobank.ua/api/merchant/pubkey"
    http_method: ClassVar[str] = "GET"

    @classmethod
    def on_json_parse(cls, response: HTTPResponse) -> Base64Encodedx509Pubkey:
        return Base64Encodedx509Pubkey(response.json()["key"])
