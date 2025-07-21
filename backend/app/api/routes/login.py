from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer

from backend.app.models.user import User

router = APIRouter(
    tags=["Login"]
)

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/login")
async def login(item: User):
    username = item.username
    password = item.password

    login = do_login(username, password)