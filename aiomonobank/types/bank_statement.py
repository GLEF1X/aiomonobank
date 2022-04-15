from typing import List, Iterator, Optional

from pydantic import Field

from aiomonobank.types.base import Base


class Transaction(Base):
    id: str
    time: int
    description: str
    mcc: int
    hold: bool
    amount: float
    operation_amount: float = Field(..., alias="operationAmount")
    currency: int = Field(..., alias="currencyCode")
    commission_rate: float = Field(..., alias="commissionRate")
    cashback_amount: float = Field(..., alias="cashbackAmount")
    balance: float
    comment: Optional[str] = None
    receipt_id: Optional[str] = Field(None, alias="receiptId")
    edrpou: Optional[str] = Field(None, alias="counterEdrpou")
    iban: Optional[str] = Field(None, alias="counterIban")


class BankStatement(Base):
    __root__: List[Transaction]

    def __iter__(self) -> Iterator[Transaction]:
        return iter(self.__root__)

    def __len__(self) -> int:
        return len(self.__root__)

    def __contains__(self, item: str) -> bool:
        return item in self.__root__
