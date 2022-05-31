from datetime import datetime
from typing import Optional, List, Union, Literal

from pydantic import HttpUrl

from aiomonobank.client.methods.acquiring.cancel_invoice import CancelInvoice, CancelInvoiceStatus
from aiomonobank.client.methods.acquiring.create_invoice import CreateInvoice, MerchantPaymentInfo
from aiomonobank.client.methods.acquiring.finalize_hold_sum import FinalizeHoldSum
from aiomonobank.client.methods.acquiring.get_invoice_status import GetInvoiceStatus, InvoiceStatus
from aiomonobank.client.methods.acquiring.get_qr_merchant_info import GetQRMerchantInfo, QRMerchantInfo
from aiomonobank.client.methods.acquiring.get_qr_merchant_list import QRMerchant, GetQRMerchantList
from aiomonobank.client.methods.acquiring.retrieve_merchant_pubkey import RetrieveMerchantPubkey, \
    Base64Encodedx509Pubkey
from aiomonobank.client.methods.bank_statement import GetBankStatement, BankStatement
from aiomonobank.client.methods.client_info import GetClientInfo, ClientInfo
from aiomonobank.client.methods.exchange_rate_list import GetExchangeRates, ExchangeRate
from aiomonobank.client.methods.set_webhook import SetWebhook
from aiomonobank.core import BaseAPIClient
from aiomonobank.core.abc.base_api_client import RequestServiceFactoryType
from aiomonobank.core.request_service import RequestServiceProto, RequestService
from aiomonobank.core.session import AiohttpSessionHolder


class MonobankAcquiringAPIClient(BaseAPIClient):

    def __init__(self, api_token: str, request_service_factory: Optional[RequestServiceFactoryType] = None, ):
        super().__init__(request_service_factory=request_service_factory)
        self._api_token = api_token

    async def create_invoice(
            self,
            amount: Union[int, str, float],
            ccy: Optional[int] = None,
            merchant_payment_info: Optional[MerchantPaymentInfo] = None,
            redirect_url: Optional[HttpUrl] = None,
            webhook_url: Optional[HttpUrl] = None,
            validity: Optional[Union[float, int, datetime]] = None,
            payment_type: Union[Literal["debit", "hold"], None] = None,
            qr_id: Optional[str] = None
    ):
        return await self._request_service.execute_api_method(
            CreateInvoice(
                amount=amount,
                ccy=ccy,
                merchant_payment_info=merchant_payment_info,
                redirect_url=redirect_url,
                webhook_url=webhook_url,
                validity=validity,
                payment_type=payment_type,
                qr_id=qr_id
            )
        )

    async def get_invoice_status(self, invoice_id: str) -> InvoiceStatus:
        return await self._request_service.execute_api_method(
            GetInvoiceStatus(invoice_id=invoice_id)
        )

    async def cancel_invoice(self, invoice_id: str, amount: Optional[int] = None) -> CancelInvoiceStatus:
        return await self._request_service.execute_api_method(
            CancelInvoice(invoice_id=invoice_id, amount=amount)
        )

    async def get_merchant_pubkey(self) -> Base64Encodedx509Pubkey:
        return await self._request_service.execute_api_method(RetrieveMerchantPubkey())

    async def finalize_hold_sum(self, invoice_id: str, amount: Optional[int] = None) -> str:
        return await self._request_service.execute_api_method(
            FinalizeHoldSum(invoice_id=invoice_id, amount=amount)
        )

    async def get_qr_merchant_info(self, merchant_id: str) -> QRMerchantInfo:
        return await self._request_service.execute_api_method(GetQRMerchantInfo(
            qr_id=merchant_id
        ))

    async def get_qr_merchant_list(self) -> List[QRMerchant]:
        return await self._request_service.execute_api_method(GetQRMerchantList())

    async def _create_request_service(self) -> RequestServiceProto:
        return RequestService(session_holder=AiohttpSessionHolder(headers={"X-Token": self._api_token}))


class MonobankAPIClient(BaseAPIClient):

    def __init__(self, api_token: str, request_service_factory: Optional[RequestServiceFactoryType] = None, ):
        super().__init__(request_service_factory=request_service_factory)
        self._api_token = api_token

    async def get_exchange_rates(self) -> List[ExchangeRate]:
        return await self._request_service.execute_api_method(GetExchangeRates())

    async def set_webhook(self, url: str) -> bool:
        is_ok = await self._request_service.execute_api_method(
            SetWebhook(webhook_url=url)  # type: ignore
        )
        return is_ok

    async def get_client_info(self) -> ClientInfo:
        return await self._request_service.execute_api_method(GetClientInfo())

    async def get_bank_statement(
            self,
            account: int = 0,
            from_date: Optional[datetime] = None,
            to_date: Optional[datetime] = None,
    ) -> BankStatement:
        return await self._request_service.execute_api_method(
            GetBankStatement(from_date=from_date, account=account, to_date=to_date)
        )

    async def _create_request_service(self) -> RequestServiceProto:
        return RequestService(session_holder=AiohttpSessionHolder(headers={"X-Token": self._api_token}))
