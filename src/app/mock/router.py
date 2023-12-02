from typing import Any
from fastapi import APIRouter

from app.mock.models import MockModel
from app.mock import service

router = APIRouter()


@router.get("/ping")
async def get_all() -> dict[str, str]:
    return {"ping": "Hello world!"}


@router.put("/")
async def save_mock(
        mock_data: MockModel
) -> dict[str, Any]:
    mock = await service.create_mock(mock_data)
    return {
        "id": mock["id"],
    }


@router.get("/all")
async def get_mocks() -> list[dict[str, Any]]:
    mocks = await service.get_all_mocks()
    return mocks
