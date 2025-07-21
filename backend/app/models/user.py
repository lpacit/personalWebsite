from pydantic import BaseModel

class User(BaseModel):
    user_email: str
    username: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDb(User):
    hashed_password: str

def get_user(user_email: str):
    pass