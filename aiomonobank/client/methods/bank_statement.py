from datetime import datetime
from typing import ClassVar, Optional

from pydantic import Field, validator

from aiomonobank.client.base import MonobankAPIMethod
from aiomonobank.types.bank_statement import BankStatement

DEFAULT_ACCOUNT_NUM = 0


class GetBankStatement(MonobankAPIMethod[BankStatement]):
    url: ClassVar[str] = "https://api.monobank.ua/personal/statement/{account}/{from}"
    http_method: ClassVar[str] = "GET"

    account: Optional[int] = Field(None, path_runtime_value=True)
    from_date: Optional[datetime] = Field(None, path_runtime_value=True, alias="from")

    @validator("account", always=True)
    def validate_account_number(cls, v: Optional[int]) -> int:
        return v or DEFAULT_ACCOUNT_NUM

    @validator("from_date", always=True)
    def validate_from_date(cls, from_date: Optional[datetime]) -> float:
        if from_date is None:
            from_date = datetime.now()

        return int(from_date.timestamp())
