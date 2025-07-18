from fastapi import APIRouter

from backend.app.models.user import User

router = APIRouter(
    tags=["Login"]
)

@router.post("/login")
async def login(item: User):
    username = item.username
    password = item.password

    login = do_login(username, password)