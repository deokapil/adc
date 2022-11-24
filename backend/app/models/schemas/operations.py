from typing import List, Optional

from pydantic import BaseModel, Field

from app.models.domain.operation import Operation
from app.models.schemas.rwschema import RWSchema

DEFAULT_ARTICLES_LIMIT = 20
DEFAULT_ARTICLES_OFFSET = 0


class OperationForResponse(RWSchema):
    operation: Operation


class OperationInResponse(RWSchema):
    operation: Operation


class OperationInCreate(RWSchema):
    sess_id: str


class ListOfOperationsInResponse(RWSchema):
    articles: List[OperationForResponse]
    articles_count: int


class OperationsFilters(BaseModel):
    author: Optional[str] = None
    limit: int = Field(DEFAULT_ARTICLES_LIMIT, ge=1)
    offset: int = Field(DEFAULT_ARTICLES_OFFSET, ge=0)
