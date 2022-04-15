from .client import MonobankClient

try:
    import uvloop

    uvloop.install()  # pragma: no cover
except ImportError:
    pass

__version__ = "0.0.1"
__maintainer__ = "GLEF1X"

__all__ = (
    "MonobankClient",
    "__version__",
    "__maintainer__"
)
