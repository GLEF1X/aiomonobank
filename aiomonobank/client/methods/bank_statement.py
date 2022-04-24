from datetime import datetime
from typing import ClassVar, Optional, Any

from pydantic import Field, validator, conint

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.core.abc.api_method import Request
from aiomonobank.types.bank_statement import BankStatement
from aiomonobank.utils.dates import convert_to_unix_time

DEFAULT_ACCOUNT_NUM = 0


class GetBankStatement(MonobankAPIMethod[BankStatement]):
    url: ClassVar[str] = "https://api.monobank.ua/personal/statement/{account}/{from}"
    http_method: ClassVar[str] = "GET"

    account: Optional[conint(ge=0)] = Field(None, path_runtime_value=True)
    from_date: Optional[datetime] = Field(None, path_runtime_value=True, alias="from")
    to_date: Optional[datetime] = Field(None, path_runtime_value=True, alias="to")

    @validator("account", always=True)
    def validate_account_number(cls, v: Optional[int]) -> int:
        return v or DEFAULT_ACCOUNT_NUM

    @validator("from_date", always=True)
    def validate_from_date(cls, from_date: Optional[datetime]) -> float:
        if from_date is None:
            from_date = datetime.now()

        return convert_to_unix_time(from_date)

    @validator("to_date", always=True)
    def validate_to_date(cls, to_date: Optional[datetime]) -> Optional[float]:
        if to_date is None:
            return None

        return convert_to_unix_time(to_date)

    def build_request(self, **url_format_kw: Any) -> "Request":
        request = super().build_request(**url_format_kw)
        if self.to_date is not None:
            request.endpoint += f"/{self.to_date}"
        return request
