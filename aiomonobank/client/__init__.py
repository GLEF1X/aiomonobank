from datetime import datetime
from typing import Optional, List, Dict, Any

from aiomonobank.client.methods.bank_statement import GetBankStatement
from aiomonobank.client.methods.client_info import GetClientInfo
from aiomonobank.client.methods.exchange_rate_list import GetExchangeRates
from aiomonobank.client.methods.set_webhook import SetWebhook
from aiomonobank.core import BaseAPIClient
from aiomonobank.core.abc.base_api_client import RequestServiceFactoryType
from aiomonobank.core.request_service import RequestServiceProto, RequestService
from aiomonobank.core.session import AiohttpSessionHolder
from aiomonobank.types.bank_statement import BankStatement
from aiomonobank.types.client_info import ClientInfo
from aiomonobank.types.exchange_rate import ExchangeRate


class MonobankClient(BaseAPIClient):

    def __init__(self, api_token: str, request_service_factory: Optional[RequestServiceFactoryType] = None, ):
        super().__init__(request_service_factory=request_service_factory)
        self._api_token = api_token

    async def get_client_info(self) -> ClientInfo:
        return await self._request_service.execute_api_method(GetClientInfo())

    async def get_exchange_rates(self) -> List[ExchangeRate]:
        return await self._request_service.execute_api_method(GetExchangeRates())

    async def set_webhook(self, webhook_url: str) -> Dict[str, Any]:
        return await self._request_service.execute_api_method(SetWebhook(webhook_url=webhook_url))

    async def get_bank_statement(
            self,
            from_date: Optional[datetime] = None,
            to_date: Optional[datetime] = None,
            account: int = 0
    ) -> BankStatement:
        return await self._request_service.execute_api_method(
            GetBankStatement(from_date=from_date, account=account)
        )

    async def _create_request_service(self) -> RequestServiceProto:
        return RequestService(session_holder=AiohttpSessionHolder(headers={"X-Token": self._api_token}))
