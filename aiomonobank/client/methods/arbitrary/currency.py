from typing import Optional, Union

from pydantic import BaseModel, BaseConfig, Field


class Currency(BaseModel):
    code: str
    decimal_digits: int
    name: str
    name_plural: str
    rounding: Union[int, float]
    symbol: str
    symbol_native: str
    iso_format: Optional[str] = Field(..., alias="isoformat")

    class Config(BaseConfig):
        frozen = True
        allow_mutation = False
