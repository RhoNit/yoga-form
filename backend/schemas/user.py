import pydantic as _pydantic
from typing import Optional

class UserBase(_pydantic.BaseModel):
    email: str

class UserCreate(UserBase):
    pass

    # class Config:
    #     orm_mode = True


# class UserShow(_pydantic.BaseModel):
#     id: str
#     name: str
#     age: int
#     email: _pydantic.EmailStr

#     class Config:
#         orm_mode = True
