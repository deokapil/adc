from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB


class UsersRepository(BaseRepository):

    async def get_user_by_username(self, *, username: str) -> UserInDB:
        user_row = await queries.get_user_by_username(
            self.connection,
            username=username,
        )
        if user_row:
            return UserInDB(**user_row)

        raise EntityDoesNotExist(
            "user with username {0} does not exist".format(username),
        )

    async def create_user(
        self,
        *,
        username: str,
        name: str,
        password: str,
    ) -> UserInDB:
        user = UserInDB(username=username, name=name)
        user.change_password(password)

        async with self.connection.transaction():
            user_row = await queries.create_new_user(
                self.connection,
                username=user.username,
                name=user.name,
                salt=user.salt,
                hashed_password=user.hashed_password,
            )

        return user.copy(update=dict(user_row))

    async def update_user(  # noqa: WPS211
        self,
        *,
        user: User,
        username: Optional[str] = None,
        name: Optional[str] = None,
        password: Optional[str] = None,
    ) -> UserInDB:
        user_in_db = await self.get_user_by_username(username=user.username)

        user_in_db.username = username or user_in_db.username
        user_in_db.email = name or user_in_db.name
        if password:
            user_in_db.change_password(password)

        async with self.connection.transaction():
            user_in_db.updated_at = await queries.update_user_by_username(
                self.connection,
                username=user.username,
                new_username=user_in_db.username,
                new_name=user_in_db.name,
                new_salt=user_in_db.salt,
                new_password=user_in_db.hashed_password,
            )

        return user_in_db
