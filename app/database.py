from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.setting import *

engine = create_engine(
    f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}",
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    return db


# 将数据库模型生成数据库中的表结构
def generate_tables():
    Base.metadata.create_all(bind=engine)
