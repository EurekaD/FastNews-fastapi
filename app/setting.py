from fastapi.security import OAuth2PasswordBearer
from urllib import parse
from dotenv import load_dotenv
import os
load_dotenv('fastnews.env')

AUTH_SCHEMA = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

ACCESS_TOKEN_EXPIRE_MINUTES = 1440

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORIthM = os.getenv('JWT_ALGORIthM')
AUTH_INIT_USER = os.getenv('AUTH_INIT_USER')
AUTH_INIT_PASSWORD = os.getenv('AUTH_INIT_PASSWORD')


DB_HOST = os.getenv('DB_HOST')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = parse.quote(os.getenv('DB_PASSWORD'))
DB_DATABASE = os.getenv('DB_DATABASE')
