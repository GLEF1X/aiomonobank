from datetime import datetime
from typing import Literal, Optional

from pydantic import Field

from aiomonobank.client.methods.base import Base


class CancelListItem(Base):
    status: Literal['processing', 'success', 'failure']
    amount_in_kopecks: Optional[int] = Field(None, alias="amount")
    ccy: Optional[int] = None
    created_date: Optional[datetime] = Field(None, alias="createdDate")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate")
    approval_code: Optional[str] = Field(None, alias="approvalCode")
    rrn: Optional[str] = None
