from typing import Optional

from asyncpg import Connection, Record
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
            article_row=operation_row,
            sess_id=sess_id,
            author_username=operation_row[AUTHOR_USERNAME_ALIAS],
            requested_user=author,
        )

    async def delete_operation(self, *, operation: Operation) -> None:
        async with self.connection.transaction():
            await queries.delete_operation(
                self.connection,
                sess_id=operation.sess_id,
                author_username=operation.user.username,
            )


    async def _get_operation_from_db_record(
        self,
        *,
        article_row: Record,
        sess_id: str,
        author_username: str,
        requested_user: Optional[User],
    ) -> Operation:
        return Operation(
            id_=article_row["id"],
            sess_id=sess_id,
            author=author_username,
            created_at=article_row["created_at"],
            updated_at=article_row["updated_at"],
        )
