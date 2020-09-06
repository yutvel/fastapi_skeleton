from fastapi import APIRouter

from fastapi_skeleton.api.routes import example

api_router = APIRouter()
api_router.include_router(example.router, tags=["base"], prefix="/base")
