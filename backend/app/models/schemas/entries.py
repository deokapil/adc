from typing import List

from app.models.domain.entry import Entries
from app.models.schemas.rwschema import RWSchema


class ListOfEntriesInResponse(RWSchema):
    entries: List[Entries]


class EntriesInResponse(RWSchema):
    entry: Entries


class EntriesInCreate(RWSchema):
    body: str
