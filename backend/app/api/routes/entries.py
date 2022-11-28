from typing import Optional

from fastapi import APIRouter, Body, Depends
from starlette import status

from app.api.dependencies.operations import get_operation_by_sess_id
from app.api.dependencies.authentication import get_current_user_authorizer

from app.api.dependencies.database import get_repository
from app.db.repositories.entries import EntryRepository
from app.models.domain.operation import Operation
from app.models.domain.users import User
from app.models.schemas.entries import (
        EntryInResponse,
        EntryInCreate
)

router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=EntryInResponse,
    name="entry:create-entry",
)
async def create_entry_for_operation(
    entry_create: EntryInCreate = Body(..., embed=True, alias="entry"),
    operation: Operation = Depends(get_operation_by_sess_id),
    user: User = Depends(get_current_user_authorizer()),
    entry_repo: EntryRepository = Depends(get_repository(EntryRepository)),
) -> EntryInResponse:
    retval = "Interesting String"
    entry = await entry_repo.create_entry_for_operation(
        info=entry_create.info,
        operation=operation,
        retval=retval
    )
    return EntryInResponse(entry=entry)

