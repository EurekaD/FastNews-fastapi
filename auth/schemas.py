from typing import Optional, Union, List
from pydantic import BaseModel


class LoginRequestForm(BaseModel):
    username: str
    password: str
    code: str
    uuid: str


class Token(BaseModel):
    token: str


class CaptchaRequestForm(BaseModel):
    uuid: str


class ImageData(BaseModel):
    base64Image: str


class User(BaseModel):
    username: str
    roles: List[str]


class ApiResponseData(BaseModel):
    code: int
    data: Union[ImageData, Token, User, None]
    message: str


class UserBase(BaseModel):
    id: Optional[int]
    username: str


class UserCreate(UserBase):
    password: str



        
