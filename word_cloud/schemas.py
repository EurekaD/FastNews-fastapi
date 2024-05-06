
from pydantic import BaseModel
from typing import Union


# 请求数据结构
class WordCloudRequestData(BaseModel):
    text: str


# 词云返回数据结构
class WordCloudData(BaseModel):
    img_bytes: str


class ApiResponseData(BaseModel):
    code: int
    data: Union[WordCloudData, None]
    message: str
