
from fastapi import APIRouter
from word_cloud.services import WordCloudService
from word_cloud.schemas import ApiResponseData, WordCloudRequestData, WordCloudData


route = APIRouter(
    tags=['词云图']
)


@route.post("/wordcloud", response_model=ApiResponseData)
async def predict(
        form: WordCloudRequestData,
):
    img_bytes = await WordCloudService.word_cloud(form.text)
    # image.save('saved_image.png')
    api_response = ApiResponseData(code=0, data=WordCloudData(img_bytes=img_bytes), message="Success")
    return api_response

