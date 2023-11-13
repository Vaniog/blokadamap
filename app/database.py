from typing import Any

from sqlalchemy import (
    Column,
    CursorResult,
    Identity,
    Insert,
    Integer,
    MetaData,
    Select,
    String,
    Table,
    Update,
)
from sqlalchemy import create_engine

from app.config import config

DATABASE_URL = str(config.DATABASE_URL)

engine = create_engine(DATABASE_URL)
metadata = MetaData()

mock_table = Table(
    "mock_table",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("data", String, nullable=False)
)


async def fetch_one(select_query: Select | Insert | Update) -> dict[str, Any] | None:
    with engine.begin() as conn:
        cursor: CursorResult = conn.execute(select_query)
        return cursor.first()._asdict() if cursor.rowcount > 0 else None


async def fetch_all(select_query: Select | Insert | Update) -> list[dict[str, Any]]:
    with engine.begin() as conn:
        cursor: CursorResult = conn.execute(select_query)
        return [r._asdict() for r in cursor.all()]


async def execute(select_query: Insert | Update) -> None:
    with engine.begin() as conn:
        await conn.execute(select_query)
