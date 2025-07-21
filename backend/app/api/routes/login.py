from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from backend.app.models.user import UserInDb, User
from backend.database.sqlite_database import Base, Session
from typing import Annotated
from backend.database.sqlite_database import engine

router = APIRouter(
    tags=["Login"]
)


def fake_hash_password(password: str):
    return "fakehashed" + password


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_user(db, user_email: str):
    query = "SELECT * FROM login WHERE user_email = :user_email"
    user = db.execute(query, {"user_email": user_email}).fetchone()
    if user:
        return UserInDb(**(user.to_dict()))
    return None


def fake_decode_token(token: str):
    # This is a placeholder for token decoding logic
    Base.metadata.create_all(bind=engine)
    db = Session()

    return get_user(db, token)


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        Base.metadata.create_all(bind=engine)
        db = Session()
        user = get_user(db, form_data.username)

        if not user or not fake_hash_password(form_data.password) == user.hashed_password:
            raise HTTPException(
                status_code=400,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"access_token": user.user_email, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user
