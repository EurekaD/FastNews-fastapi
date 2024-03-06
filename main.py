import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.setting import AUTH_SCHEMA
from app.database import generate_tables
from fastapi.responses import RedirectResponse
from auth.router import route as auth_router
from auth.services import init_admin_user

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth_router,
    prefix="/api/v1"
)

generate_tables()
init_admin_user()

if __name__ == '__main__':
    uvicorn.run(app=app)