import asyncio
import warnings
from typing import Optional


def get_running_loop(
        loop: Optional[asyncio.AbstractEventLoop] = None,
) -> asyncio.AbstractEventLoop:
    if loop is None:
        loop = asyncio.get_event_loop()
    if not loop.is_running():
        warnings.warn(
            "The object should be created within an async function",
            DeprecationWarning,
            stacklevel=3,
        )
    return loop
