from fastapi import APIRouter

from routes import curriculum

api_router = APIRouter()

api_router.include_router(curriculum.router)