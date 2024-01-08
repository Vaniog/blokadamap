from fastapi import FastAPI

from app.authors.models import init as init_authors
from app.base.models import Base
from app.database import engine
from app.notes.models import init as init_notes
from app.point.models import init as init_point

# заглушки (чтобы не было ошибок о неиспользуемых импортах)
# для создания таблиц обязательно импортировать файлы с моделями
init_authors()
init_notes()
init_point()
Base.metadata.create_all(bind=engine)

app = FastAPI()
