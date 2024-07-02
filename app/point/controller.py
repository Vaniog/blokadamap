from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union
from pydantic import BaseModel
from starlette import status
from fastapi.openapi.models import Response as OpenApiResponse

from app.database import get_db
from app.point.dto import CoordinatesDTO, PointDTO, PointResponseDTO, BaseResponse, ReducedPointDTO, PointFilterDTO, PointCoordinatesDTO
from app.point.service import PointService
from app.notes.dtos import ReducedNoteDTO

router = APIRouter(prefix="/points")

class EmptyResponse(BaseModel):
    pass
    
@router.post(
    "/",
    tags=["points"],
    status_code = status.HTTP_200_OK,
    response_model = BaseResponse,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def create(dto: PointDTO, db: Session = Depends(get_db)):
    dto.validate_ids(db)
    service = PointService(db)
    service.create(dto)
    return BaseResponse(description="Point was added successfully")


@router.get(
    "/{id}",
    tags=["points"],
    status_code=status.HTTP_200_OK,
    response_model = Union[PointDTO, ReducedPointDTO],
    responses = {
        status.HTTP_200_OK: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "schema": {
                        "oneOf": [
                            {"$ref": "#/components/schemas/ReducedPointDTO"},
                            {"$ref": "#/components/schemas/PointDTO"},
                        ]
                    },
                    "examples": {
                        "Reduced": {
                            "summary": "Reduced response",
                            "value": ReducedPointDTO.Config.schema_extra["example"]
                        },
                        "Full": {
                            "summary": "Full response",
                            "value": PointDTO.Config.schema_extra["example"]
                        }
                    }   
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Point not found",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def get_one(id: int, extended: bool = True, db: Session = Depends(get_db)):
    service = PointService(db)
    res = service.get_by_id(id, extended)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Point not found"
        )
    return res


@router.post(
    "/{id}/coordinates",
    tags=["points"],
    status_code=status.HTTP_200_OK,
    response_model=BaseResponse,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Point not found",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def create_coordinates(dto: CoordinatesDTO, id: int, db: Session = Depends(get_db)):
    service = PointService(db)
    if not service.exists(id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Point not found"
        )
    service.create_coordinates(id, dto)
    return BaseResponse(description="Point was added successfully")



@router.get(
    "/{id}/notes",
    tags=["points"],
    status_code=status.HTTP_200_OK,
    response_model=ReducedNoteDTO,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Notes not found",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def get_notes(id: int, db: Session = Depends(get_db)):
    service = PointService(db)
    res = service.get_notes(id)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Notes not found"
        )
    return res


@router.get(
    "/{id}/coordinates",
    response_model=PointCoordinatesDTO,
    status_code=status.HTTP_200_OK,
    tags=["points"],
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def get_coordinates(id: int, db: Session = Depends(get_db)):
    service = PointService(db)
    return service.get_coordinates(id)


@router.get(
    "/filters",
    tags=["points"],
    response_model=PointFilterDTO,
    status_code=status.HTTP_200_OK,
)
def get_filters(db: Session = Depends(get_db)):
    service = PointService(db)
    return service.get_filters()


@router.get(
    "/",
    tags=["points"],
    status_code = status.HTTP_200_OK,
    response_model=List[PointResponseDTO],
)
def get_all(db: Session = Depends(get_db)):
    service = PointService(db)
    return service.get_all()
