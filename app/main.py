from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.authors.controller import router as authors_router
from app.authors.models import init as init_authors
from app.base.models import Base
from app.database import engine
from app.notes.controller import router as notes_router
from app.notes.models import init as init_notes
from app.point.controller import router as points_router
from app.point.models import init as init_point


def init_db():
    # заглушки (чтобы не было ошибок о неиспользуемых импортах)
    # для создания таблиц обязательно импортировать файлы с моделями
    init_authors()
    init_notes()
    init_point()
    Base.metadata.create_all(bind=engine)
    print("database initialized")

tags_metadata = [
    {
        "name": "authors",
    },
    {
        "name": "notes",
    },
    {
        "name": "points",
    },
]

description = """
**"Блокадная карта"** - проект, цель которого - рассказать о блокаде Ленинграда от первого лица, поместив на интерактивную карту цитаты из дневников
ленинградцев, свидетельствующие о том, **что, где и когда** произошло в пространстве осажденного города.

Разработан студентами ИТМО под руководством преподавателей Центра социальных и гуманитарных наук ИТМО Н.Д. Пригодича, А. Ф. Павловского.
Проект реализуется в сотрудничестве с Центром изучения эго-документов **"Прожито"** Европейского университета в Санкт-Петербурге.
"""

init_db()
app = FastAPI(
    version="0.1.0",
    openapi_tags=tags_metadata,
    description=description,
    license_info={
        "name": "Documentation",
        "url": "https://docs.google.com/document/d/1a1vIpdnPGrJ7OpoXy6PB1PduKu4MXXtSNk7K5TG2wCU/edit#heading=h.qm20hkvowj3w",
    },
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        license_info=app.license_info,
        routes=app.routes,
    )
    openapi_schema["openapi"] = "3.0.0"  # Change the OpenAPI version to 3.0.0
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# TODO: PATCH endpoints
app.include_router(authors_router)
app.include_router(notes_router)
app.include_router(points_router)
