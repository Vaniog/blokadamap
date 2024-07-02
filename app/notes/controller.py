from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import List, Union

from app.database import get_db
from app.notes.dtos import NoteDTO, TagDTO, BaseResponse, NoteFiltersDTO, NoteResponseDTO, ReducedNoteResponseDTO
from app.notes.service import NoteService

router = APIRouter(prefix="/notes")


@router.get(
    "/filters",
    tags=["notes"],
    status_code = status.HTTP_200_OK,
    response_model=NoteFiltersDTO
)
def get_filters(db: Session = Depends(get_db)):
    service = NoteService(db)
    return service.get_filters()


@router.get(
    "/",
    tags=["notes"],
    status_code = status.HTTP_200_OK,
    response_model=List[NoteResponseDTO]
)
def get_all(db: Session = Depends(get_db)):
    service = NoteService(db)
    return service.get_all()


@router.get(
    "/{id}",
    tags=["notes"],
    status_code = status.HTTP_200_OK,
    response_model = Union[NoteDTO, ReducedNoteResponseDTO],
    responses = {
        status.HTTP_200_OK: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "schema": {
                        "oneOf": [
                            {"$ref": "#/components/schemas/ReducedNoteResponseDTO"},
                            {"$ref": "#/components/schemas/NoteDTO"},
                        ]
                    },
                    "examples": {
                        "Reduced": {
                            "summary": "Reduced response",
                            "value": ReducedNoteResponseDTO.Config.schema_extra["example"]
                        },
                        "Full": {
                            "summary": "Full response",
                            "value": NoteDTO.Config.schema_extra["example"]
                        }
                    }   
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Note/point not found",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def get_one(id: int, extended: bool = True, db: Session = Depends(get_db)):
    service = NoteService(db)
    res = service.get_by_id(id, extended)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note/point not found"
        )
    return res


@router.post(
    "/",
    tags=["notes"],
    status_code = status.HTTP_200_OK,
    response_model=BaseResponse,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Bad request",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def create(note: NoteDTO, db: Session = Depends(get_db)):
    note.validate_ids(db)
    service = NoteService(db)
    try:
        created_note = service.create_note(note)
        return created_note
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )


@router.post(
    "/tags",
    tags=["notes"],
    status_code = status.HTTP_200_OK,
    response_model=BaseResponse,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def create_tag(tag: TagDTO, db: Session = Depends(get_db)):
    service = NoteService(db)
    service.create_tag(tag)
