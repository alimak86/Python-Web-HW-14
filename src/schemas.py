from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic import EmailStr

class ResponseContactModel(BaseModel):
  # """
  # Defines response for the Contact Model

  # Parameters :
  # : id : int
  # : firstname : str
  # : secondname : str
  # : email : str
  # : phonenumber : str
  # : dateofbirth : str
  # """
  id: int = Field(default=1, ge=1)
  firstname: str = Field(max_length=50)
  secondname: str = Field(max_length=50)
  email: str = Field(max_length=50)
  phonenumber: str = Field(max_length=50)
  dateofbirth: str = Field(max_length=50)


class ContactModel(BaseModel):
# """
# Contact model without id field
# """
  firstname: str = Field(max_length=50)
  secondname: str = Field(max_length=50)
  email: str = Field(max_length=50)
  phonenumber: str = Field(max_length=50)
  dateofbirth: str = Field(max_length=50)


class ContactModelFullName(BaseModel):
  # """
  # Response Contact model
  # Parameters:
  # : firstname : str
  # : secondname : str
  # """
  firstname: str = Field(max_length=50)
  secondname: str = Field(max_length=50)


class UserModel(BaseModel):
# """
# User response model
# Parameters:
# : username : str
# : email : str
# : password : str
# """
  username: str = Field(min_length=5, max_length=16)
  email: str
  password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
  # """
  # User response model
  # Parameters:
  # : id : int
  # : username : str
  # : email : str
  # : created_at : datetime
  # : avatar : str
  # """
  id: int
  username: str
  email: str
  created_at: datetime
  avatar: str

  class Config:
    orm_mode = True


class UserResponse(BaseModel):
  # """
  # User response model
  # Parameters:
  # : user  : User
  # : detail : str
  # """
  user: UserDb
  detail: str = "User successfully created"


class TokenModel(BaseModel):
  # """
  # Token response model
  # Parameters:
  # : access_token : str
  # : refresh_token : str
  # : token_type : str
  # """
  access_token: str
  refresh_token: str
  token_type: str = "bearer"

class RequestEmail(BaseModel):
  # """
  # Email request model
  # Parameters:
  # : email : EmailStr
  # """
    email: EmailStr