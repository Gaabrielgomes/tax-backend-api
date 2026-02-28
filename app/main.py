from fastapi import FastAPI

from app.database import engine, Base
from app.routes.client import router as client_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    client_router,
    prefix="/clients",
    tags=["Clients"]
)