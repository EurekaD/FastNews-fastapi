import datetime
from starlette import status
from app.setting import JWT_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
import jwt
from jwt import PyJWTError
from fastapi import HTTPException


def create_token(data):
    # 设置 JWT 的有效期
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # 构建 JWT 的 payload
    payload = {
        'user_id': data['username'],
        'exp': expiration_time
    }

    # 使用 PyJWT 库生成 JWT
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return token


# 创建提取用户名的函数
def extract_token(token: str):
    try:
        # 使用 PyJWT 解码 JWT
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        # 从 payload 中提取出用户名
        username = payload.get("user_id")
        return username
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的令牌",
            headers={"WWW-Authenticate": "Bearer"},
        )


# 每次输出的token字符串不相同
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE3MDg0MDMzMTN9.2tkBFk_VPdozIJSOCMAOSTBIHokA-tCHgMAaAenkwXU
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE3MDg0MDMzMjV9.ZWn8OMmyGcNUOg7IhMxBxdC9Lx0xEpeHzr9vqMJ6p3U
if __name__ == "__main__":
    token = create_token(data={"username": "hcenlin"})
    username = extract_token(token)
    print(username)
