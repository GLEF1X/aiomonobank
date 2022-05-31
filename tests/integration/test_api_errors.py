import pytest

from aiomonobank import MonobankAPIClient
from aiomonobank.client.exceptions import MonobankAPIError


@pytest.mark.slow
async def test_raises_if_api_key_is_wrong():
    monobank = MonobankAPIClient(api_token="wrong token")

    with pytest.raises(MonobankAPIError):
        await monobank.get_client_info()
