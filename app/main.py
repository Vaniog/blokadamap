from fastapi import FastAPI

from app.base.models import Base
from app.authors.models import *
from app.notes.models import *
from app.point.models import *
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
