from db.models.user import User
from schemas.user import UserCreate 
import db.services as _services

import fastapi as _fastapi

import sqlalchemy.orm as _orm

router = _fastapi.APIRouter()

@router.post("/user")
def create_user(user: UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    # user_obj = await _services.get_user_by_email(user.email, db)

    # if user_obj:
    #     raise _fastapi.HTTPException(status_code=400, detail="Email already in use")
    # print(user.email)
    
    # return await _services.create_user(user, db)

    user_obj = User(
        # name=user.name,
        email=user.email,
        # age=user.age
    )

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
