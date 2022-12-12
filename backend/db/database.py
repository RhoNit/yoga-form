from typing import Generator

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

from db.config import setting


SQLALCHEMY_DATABASE_URL = setting.DATABASE_URL
# SQLALCHEMY_DATABASE_URL = "sqlite:///./store.db"

engine  = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL
    # connect_args={"check_same_thread": False}
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
