from fastapi import APIRouter, Depends
from auth.captcha import Captcha
from model.services import get_model, Summarization
from .schemas import AbstractRequestData, ApiResponseData, Text

CAPTCHA = Captcha()

route = APIRouter(
    tags=['摘要']
)


@route.post("/abstract", response_model=ApiResponseData)
async def predict(
        form: AbstractRequestData,
        model: Summarization = Depends(get_model)
):
    print(form.text)
    abstract_text = await model.predict(form.text)

    api_response = ApiResponseData(code=0, data=Text(abstract_text=abstract_text), message="Success")
    print(api_response)
    return api_response

@route.post("/abstract_para", response_model=ApiResponseData)
async def predict(
        form: AbstractRequestData,
        model: Summarization = Depends(get_model)
):
    print(form.text)
    abstract_text = await model.predict_paragraphing(form.text)

    api_response = ApiResponseData(code=0, data=Text(abstract_text=abstract_text), message="Success")
    print(api_response)
    return api_response