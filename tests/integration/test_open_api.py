import pytest

from aiomonobank.types.bank_statement import BankStatement
from aiomonobank.types.client_info import ClientInfo
from aiomonobank.types.exchange_rate import ExchangeRate

pytestmark = pytest.mark.anyio


async def test_get_client_info(monobank_client):
    client_info = await monobank_client.get_client_info()
    assert isinstance(client_info, ClientInfo)


async def test_exchange_rate(monobank_client):
    exchange_rates = await monobank_client.get_exchange_rates()
    assert all(isinstance(rate, ExchangeRate) for rate in exchange_rates)


async def test_get_bank_statement(monobank_client):
    statement = await monobank_client.get_bank_statement()
    assert isinstance(statement, BankStatement)
