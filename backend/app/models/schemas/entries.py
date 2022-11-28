from typing import List

from app.models.domain.entry import Entry
from app.models.schemas.rwschema import RWSchema


class ListOfEntriesInResponse(RWSchema):
    entries: List[Entry]


class EntryInResponse(RWSchema):
    entry: Entry


class EntryInCreate(RWSchema):
    info: str

