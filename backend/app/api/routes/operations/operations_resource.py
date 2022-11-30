import uuid
import random
from fastapi import APIRouter, Body, Depends, HTTPException, Response
from starlette import status

from app.api.dependencies.authentication import get_current_user_authorizer
from app.api.dependencies.database import get_repository
from app.db.repositories.operations import OperationRepository
from app.models.domain.users import User
from app.models.schemas.operations import (
    OperationInResponse, OperationNextInResponse,

)
router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=OperationInResponse,
    name="operations:create-operation",
)
async def create_new_operation(
    user: User = Depends(get_current_user_authorizer()),
    operation_repo: OperationRepository = Depends(get_repository(OperationRepository)),
) -> OperationInResponse:
    # create session id
    sess_id = uuid.uuid4().hex
    operation = await operation_repo.create_operation(
        sess_id=sess_id,
        author=user,
    )
    return OperationInResponse(operation=operation)

@router.post(
    "/next",
    status_code=status.HTTP_201_CREATED,
    response_model=OperationNextInResponse,
    name="operations:create-operation-next",
)
async def create_next_operation(
        user: User = Depends(get_current_user_authorizer()),
        operation_repo: OperationRepository = Depends(get_repository(OperationRepository))
) -> OperationNextInResponse:
    alpha = ["A", "B", "C", "D", "E", "F"]
    return OperationNextInResponse(bucket=random.choice(alpha),
                                   envelops=["first", "second", "third"],
                                   counts={"A": 1,
                                           "B": 4,
                                           "C": 7,
                                           "D": 10,
                                           "E": 5,
                                           "F": 8,
                                           "G": 12,
                                           "H": 15,
                                           "I": 11,
                                           "J": 8
                                           }
                                   )
