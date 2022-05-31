from .client import MonobankAPIClient, MonobankAcquiringAPIClient

__version__ = "0.0.1"

__acquiring_api_version__ = "v2204"
__api_version__ = "v2205"

__all__ = (
    "MonobankAPIClient",
    "MonobankAcquiringAPIClient",
    "__version__",
    "__acquiring_api_version__",
    "__api_version__",
)
