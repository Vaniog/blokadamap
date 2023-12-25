from fastapi import FastAPI

from app.base.models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
