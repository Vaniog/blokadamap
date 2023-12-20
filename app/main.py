from fastapi import FastAPI

from app.database import engine, metadata

metadata.create_all(bind=engine)

app = FastAPI()
# app.include_router(mock_router, prefix="/records")
# закомиться пж
