from fastapi import Depends, HTTPException, Path
from starlette import status

from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.database import get_repository
from app.db.errors import EntityDoesNotExist
from app.db.repositories.operations import OperationRepository
from app.models.domain.operation import Operation
from app.models.domain.users import User

from app.resources import strings


async def get_operation_by_sess_id(
    sess_id: str = Path(..., min_length=1),
    operation_repo: OperationRepository = Depends(get_repository(OperationRepository)),
) -> Operation:
    try:
        return await operation_repo.get_operation_by_sess_id(sess_id=sess_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.ARTICLE_DOES_NOT_EXIST_ERROR,
        )
