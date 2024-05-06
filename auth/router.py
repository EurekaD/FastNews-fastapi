from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.setting import AUTH_SCHEMA
from utils.token import create_token
from .schemas import Token, User, UserCreate, CaptchaRequestForm, ApiResponseData, ImageData, LoginRequestForm
from .services import authenticate_user, get_user, get_current_user, create_user
from utils.login_code_gen import gen_captcha_text_and_image
from auth.captcha import Captcha

CAPTCHA = Captcha()

route = APIRouter(
    tags=['登录']
)


@route.post("/login", response_model=ApiResponseData)
async def login(
        form: LoginRequestForm,
        db: Session = Depends(get_db)
):
    # 先确认验证码正确
    flag = CAPTCHA.verify(form.uuid, form.code)
    print(flag)
    if flag:
        user = authenticate_user(db, form.username, form.password)
        print(user)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="用户名或密码无效",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = create_token(data={"username": user.username})
        api_response = ApiResponseData(code=0, data=Token(token=access_token), message="Success")
        return api_response
    else:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="验证码输入错误",
        )


# @route.post("/createuser", dependencies=[Depends(AUTH_SCHEMA)])
@route.post("/createuser")
async def createuser(user: UserCreate, db: Session = Depends(get_db)):
    dbuser = get_user(db, user.username)
    print(dbuser)
    if dbuser:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="用户名已存在",
        )
    if create_user(db, user) is not None:
        api_response = ApiResponseData(code=0, data=None, message="Success Create User")
        return api_response


# 验证码流程如下：
# 1. 前端发送get请求来获取验证码图片。需要前端生成uuid并把uuid的值传到后端；
# 2. 后端收到前端的生成验证码请求，生成验证码图片和验证码内容。然后将前端传递过来的uuid值作为键，验证码内容作为值，形成一对键值对，存储在Redis中。同时根据需求设置验证码的有效期。
# 3. 前端获取到验证码，等待用户输入验证码之后进行提交请求。提交请求中包含用户输入的验证码以及刚才生成的uuid。
# 4. 后端拿到uuid以及用户输入的验证码内容。根据uuid取出Redis中保存的值，如果值为空，那么说明验证码已经过期；
#    如果值不为空，取出值和前端传过来的用户输入的验证码内容进行比价，如果相等，那么就验证码输入正确，否则验证输入错误，将结果返回给前端。
# 5. 前端收到后的响应，如果验证码正确，则显示提交成功，否则重新请求后端生成验证码，然后重复上述步骤。

@route.post("/login/code")
async def gen_code(cap: CaptchaRequestForm, captcha=Depends(gen_captcha_text_and_image)):
    captcha_text = captcha['captcha_text']
    base64_encoded_image = captcha['captcha_image']
    # 暂时不使用redis,
    uuid = cap.uuid
    CAPTCHA.append(uuid, captcha_text)
    api_response = ApiResponseData(code=0, data=ImageData(base64Image=base64_encoded_image), message="Success")
    return api_response


@route.get("/userinfo", response_model=ApiResponseData)
async def userinfo(user: User = Depends(get_current_user)):
    api_response = ApiResponseData(code=0, data=user, message="Success")
    return api_response

