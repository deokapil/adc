from typing import Optional

from asyncpg import Connection, Record

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries

from app.db.repositories.base import BaseRepository
from app.models.domain.operation import Operation
from app.models.domain.users import User

AUTHOR_USERNAME_ALIAS = "author_username"
SLUG_ALIAS = "slug"

CAMEL_OR_SNAKE_CASE_TO_WORDS = r"^[a-z\d_\-]+|[A-Z\d_\-][^A-Z\d_\-]*"


class OperationRepository(BaseRepository):  # noqa: WPS214
    def __init__(self, conn: Connection) -> None:
        super().__init__(conn)

    async def get_operation_by_sess_id(
            self,
            *,
            sess_id: str,
    ) -> Operation:
        operation_row = await queries.get_operation_by_session(self.connection, sess_id=sess_id)
        if operation_row:
            return await self._get_operation_from_db_record(
                operation_row=operation_row,
            )

        raise EntityDoesNotExist("article with slug {0} does not exist".format(sess_id))

    async def create_operation(  # noqa: WPS211
        self,
        *,
        sess_id: str,
        author: User,
    ) -> Operation:
        async with self.connection.transaction():
            operation_row = await queries.create_new_operation(
                self.connection,
                sess_id=sess_id,
                author_username=author.username,
            )

        return await self._get_operation_from_db_record(
            operation_row=operation_row,
        )

    async def delete_operation(self, *, operation: Operation) -> None:
        async with self.connection.transaction():
            await queries.delete_operation(
                self.connection,
                sess_id=operation.sess_id,
                author_username=operation.author,
            )

    async def _get_operation_from_db_record(
        self,
        *,
        operation_row: Record
    ) -> Operation:
        return Operation(
            id_=operation_row["id"],
            sess_id=operation_row["sess_id"],
            author=operation_row["author_username"],
            created_at=operation_row["created_at"],
            updated_at=operation_row["updated_at"],
        )
