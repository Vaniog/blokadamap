from fastapi import FastAPI

from app.mock.router import router as mock_router

from app.database import engine
from app.database import metadata

metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(mock_router, prefix="/records")
