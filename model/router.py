from fastapi import APIRouter, Depends
from auth.captcha import Captcha
from model.services import get_model, Summarization


CAPTCHA = Captcha()

route = APIRouter(
    tags=['摘要']
)

@route.post("/sumraize", response_model=ApiResponseData)
async def predict(
        form: LoginRequestForm,
        model: Summarization = Depends(get_model)
):
    text =
    return model.predict()