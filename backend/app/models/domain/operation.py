from typing import List

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.rwmodel import RWModel


class Operation(IDModelMixin, DateTimeModelMixin, RWModel):
    sess_id: str
    author: str
