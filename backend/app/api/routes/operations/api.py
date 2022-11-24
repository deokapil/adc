from fastapi import APIRouter

from app.api.routes.operations import operations_common, operations_resource

router = APIRouter()

router.include_router(operations_common.router, prefix="/operations")
router.include_router(operations_resource.router, prefix="/operations")
