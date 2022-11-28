from typing import List, Optional

from asyncpg import Connection, Record

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.operation import Operation
from app.models.domain.entry import Entry
from app.models.domain.users import User


class EntryRepository(BaseRepository):
    def __init__(self, conn: Connection) -> None:
        super().__init__(conn)

    async def get_entry_by_id(
        self,
        *,
        entry_id: int,
    ) -> Entry:
        entry_row = await queries.get_entry_by_id(
            self.connection,
            entry_id=entry_id,
        )
        if entry_row:
            return await self._get_entry_from_db_record(
                entry_row=entry_row
            )

        raise EntityDoesNotExist(
            "comment with id {0} does not exist".format(entry_id),
        )

    async def get_entries_for_operation(
        self,
        *,
        operation: Operation,
        user: Optional[User] = None,
    ) -> List[Entry]:
        entry_rows = await queries.get_entries_for_operation_by_sess_id(
            self.connection,
            sess_id=operation.sess_id,
        )
        return [
            await self._get_entry_from_db_record(
                entry_row=entry_row,
            )
            for entry_row in entry_rows
        ]

    async def create_entry_for_operation(
        self,
        *,
        info: str,
        operation: Operation,
        retval: str,
    ) -> Entry:
        # check if sess_id
        entry_row = await queries.create_new_entry(
            self.connection,
            info=info,
            sess_id=operation.sess_id,
            retval=retval
        )
        return await self._get_entry_from_db_record(
            entry_row=entry_row,
        )

    async def delete_entry(self, *, entry: Entry) -> None:
        await queries.delete_entry_by_id(
            self.connection,
            entry_id=entry.id_
        )

    async def _get_entry_from_db_record(
        self,
        *,
        entry_row: Record,
    ) -> Entry:
        return Entry(
            id_=entry_row["id"],
            info=entry_row["info"],
            retval=entry_row["retval"],
            sess_id=entry_row["sess_id"],
            created_at=entry_row["created_at"],
            updated_at=entry_row["updated_at"],
        )
