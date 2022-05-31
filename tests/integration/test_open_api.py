import pytest

from aiomonobank.client import BankStatement, ClientInfo, ExchangeRate

pytestmark = pytest.mark.anyio


@pytest.mark.slow
async def test_get_client_info(monobank_client):
    client_info = await monobank_client.get_client_info()
    assert isinstance(client_info, ClientInfo)


@pytest.mark.slow
async def test_exchange_rate(monobank_client):
    exchange_rates = await monobank_client.get_exchange_rates()
    assert all(isinstance(rate, ExchangeRate) for rate in exchange_rates)


@pytest.mark.slow
async def test_get_bank_statement(monobank_client):
    statement = await monobank_client.get_bank_statement()
    assert isinstance(statement, BankStatement)
