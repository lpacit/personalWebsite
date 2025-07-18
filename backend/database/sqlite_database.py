from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from decouple import config

from backend.env import DATABASE_PATH

sqlite_path = config("DATABASE_PATH", default=DATABASE_PATH)
SQL_ALCHEMY_DATABASE_URI = f"sqlite:///{sqlite_path}"
engine = create_engine(
    SQL_ALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)