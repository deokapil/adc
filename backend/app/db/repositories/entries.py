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
        operation: Operation,
        user: Optional[User] = None,
    ) -> Entry:
        entry_row = await queries.get_entry_by_id(
            self.connection,
            entry_id=entry_id,
        )
        if entry_row:
            return await self._get_entry_from_db_record(
                entry_row=entry_row,
                author_username=entry_row["author_username"],
                requested_user=user,
            )

        raise EntityDoesNotExist(
            "comment with id {0} does not exist".format(entry_id),
        )

    async def get_comments_for_article(
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
                author_username=entry_row["author_username"],
                requested_user=user,
            )
            for entry_row in entry_rows
        ]

    async def create_entry_for_operation(
        self,
        *,
        info: str,
        operation: Operation,
        user: User,
    ) -> Entry:
        entry_row = await queries.create_new_entry(
            self.connection,
            info=info,
            sess_id=operation.sess_id,
            author_username=user.username,
        )
        return await self._get_entry_from_db_record(
            entry_row=entry_row,
            author_username=entry_row["author_username"],
            requested_user=user,
        )

    async def delete_entry(self, *, entry: Entry) -> None:
        await queries.delete_entry_by_id(
            self.connection,
            entry_id=entry.id_,
            author_username=entry.ops.user.username,
        )

    async def _get_entry_from_db_record(
        self,
        *,
        entry_row: Record,
        author_username: str,
        requested_user: Optional[User],
    ) -> Entry:
        return Entry(
            id_=entry_row["id"],
            info=entry_row["info"],
            author=author_username,
            created_at=entry_row["created_at"],
            updated_at=entry_row["updated_at"],
        )
