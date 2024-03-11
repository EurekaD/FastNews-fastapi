from pydantic import BaseModel
from typing import Optional, Union, List


class AbstractRequestData(BaseModel):
    text: str


class Text(BaseModel):
    abstract_text: str


class ApiResponseData(BaseModel):
    code: int
    data: Union[Text, None]
    message: str
