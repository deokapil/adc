from fastapi import APIRouter
from app.api.routes.operations import api as operations
from app.api.routes import authentication, users
from app.api.routes import entries

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/auth")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(operations.router, tags=["operations"])
router.include_router(entries.router, tags=["entries"], prefix="/operations/{sess_id}/entries",)
