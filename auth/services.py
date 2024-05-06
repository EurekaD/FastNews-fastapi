from fastapi import Depends, HTTPException, status
from sqlalchemy import func
from app.setting import *
from app.database import get_db
from .models import UserInDB
from .schemas import UserCreate, User
from utils.password import get_password_hash, verify_password
from utils.token import extract_token
from sqlalchemy.orm import Session
from jwt import PyJWTError


def init_admin_user():
    db = get_db()
    print(type(db))
    cnt = db.query(func.count(UserInDB.username)).scalar()

    if cnt == 0:
        user = UserInDB(
            username=AUTH_INIT_USER,
            hashed_password=get_password_hash(AUTH_INIT_PASSWORD)
        )
        db.add(user)
        db.commit()
    db.close()


def get_user(db: Session, username: str):
    return db.query(UserInDB).filter(UserInDB.username == username).first()


def create_user(db: Session, user: UserCreate):
    salt, hashed_password = get_password_hash(user.password)
    db_user = UserInDB(
        username=user.username,
        hashed_password=hashed_password,
        salt=salt,
        roles='0'
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# 验证用户名和密码是否正确
def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password, user.salt):
        return False
    return user


# 获取当前用户信息，用户名
async def get_current_user(
        token: str = Depends(AUTH_SCHEMA),
        db: Session = Depends(get_db)
):
    invalid_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="无效的用户依据",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        username: str = extract_token(token)
        if username is None:
            raise invalid_exception
    except PyJWTError:
        raise invalid_exception
    user_db = get_user(db, username=username)
    if user_db is None:
        raise invalid_exception
    if user_db.roles == "0":
        user = User(username=user_db.username, roles=["user"])
        return user
    else:
        user = User(username=user_db.username, roles=["admin"])
        return user
