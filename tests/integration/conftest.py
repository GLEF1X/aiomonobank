import asyncio
import os
from typing import Generator

import pytest

from aiomonobank.client import MonobankClient

pytestmark = pytest.mark.anyio


@pytest.fixture(scope="session")
def event_loop() -> asyncio.AbstractEventLoop:
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(params=[
    pytest.param(('asyncio', {'use_uvloop': True}), id='asyncio+uvloop'),
    pytest.param(('asyncio', {'use_uvloop': False}), id='asyncio'),
    pytest.param(('trio', {'restrict_keyboard_interrupt_to_checkpoints': True}), id='trio')
])
def anyio_backend(request: pytest.FixtureRequest):
    return request.param  # type: ignore


@pytest.fixture(scope="session")
def api_token() -> str:
    token = os.environ.get("MONOBANK_API_TOKEN")
    if not token:
        raise RuntimeError("MONOBANK_API_TOKEN is not set")

    return token


@pytest.fixture(scope="session")
async def monobank_client(api_token: str) -> MonobankClient:
    client = MonobankClient(api_token)
    yield client
    await client.close()
