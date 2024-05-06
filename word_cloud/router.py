
from fastapi import APIRouter
from word_cloud.services import WordCloudService
from word_cloud.schemas import ApiResponseData, WordCloudRequestData, WordCloudData
from utils.image_encoder import pil_to_bytes

route = APIRouter(
    tags=['词云图']
)


@route.post("/wordcloud", response_model=ApiResponseData)
async def predict(
        form: WordCloudRequestData,
):
    image = await WordCloudService.word_cloud(form.text)
    img_bytes = pil_to_bytes(image)
    # image.save('saved_image.png')
    api_response = ApiResponseData(code=200, data=WordCloudData(img_bytes=img_bytes), message="Success")
    return api_response

