from fastapi.security import OAuth2PasswordBearer
from urllib import parse

AUTH_SCHEMA = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

JWT_SECRET_KEY = '060ccccf7c2e4d0f7de9128670ed3d7ba8df0251ec0dca51f3fc76fc9e218ef7'
JWT_ALGORIthM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1440
AUTH_INIT_USER = 'root'
AUTH_INIT_PASSWORD = 'chenlin'


DB_HOST = 'localhost'
DB_USERNAME = 'root'
DB_PASSWORD = parse.quote('chenlin')
DB_DATABASE = 'fastnews'
