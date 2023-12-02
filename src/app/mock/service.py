from typing import Any
from sqlalchemy import insert, select
from app.database import fetch_one, fetch_all
from app.mock.models import MockModel

from app.database import mock_table


async def create_mock(mock: MockModel) -> dict[str, Any] | None:
    insert_query = (
        insert(mock_table)
        .values(
            {
                "data": mock.data
            }
        )
        .returning(mock_table)
    )

    return await fetch_one(insert_query)


async def get_all_mocks() -> list[dict[str, str]] | None:
    select_query = select(mock_table)

    return await fetch_all(select_query)


async def get_mock_by_id(mock_id: int) -> dict[str, Any] | None:
    select_query = select(mock_table).where(mock_table.c.id == mock_id)

    return await fetch_one(select_query)
