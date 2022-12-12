from typing import Generator
import db.database as _database

import sqlalchemy.orm as _orm
from db.models.user import User
from schemas.user import UserCreate


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db() -> Generator:
    try:
        db = _database.SessionLocal()
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(User).filter(User.email == email).first()


# async def create_user(user: UserCreate, db: _orm.Session):
#     user_obj = User(
#         name=user.name,
#         email=user.email,
#         age=user.age
#     )

#     db.add(user_obj)
#     db.commit()
#     db.refresh(user_obj)
#     return user_obj