from decouple import config
from backend.app.env import DATABASE_PATH

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_path = config("DATABASE_PATH", default=DATABASE_PATH)
SQL_ALCHEMY_DATABASE_URI = f"sqlite:///{sqlite_path}"
engine = create_engine(
    SQL_ALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()