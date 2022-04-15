import pytest

from aiomonobank import MonobankClient
from aiomonobank.client.exceptions import MonobankAPIError


async def test_raises_if_api_key_is_wrong():
    monobank = MonobankClient(api_token="wrong token")

    with pytest.raises(MonobankAPIError):
        await monobank.get_client_info()
