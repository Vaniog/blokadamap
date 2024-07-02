from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from typing import List, Union

from app.authors.dtos import AuthorDTO
from app.authors.service import AuthorService
from app.database import get_db
from app.authors.dtos import AuthorFilterDTO, AuthorDTO, BaseResponse, ReducedAuthorResponseDTO, AuthorResponseDTO

router = APIRouter(prefix="/authors")


@router.get(
    "/filters",
    tags=["authors"],
    status_code=status.HTTP_200_OK,
    response_model=AuthorFilterDTO
)
def get_filters(db: Session = Depends(get_db)):
    author_service = AuthorService(db)
    return author_service.get_filters()


@router.get(
    "/",
    tags=["authors"],
    status_code=status.HTTP_200_OK,
    response_model=List[AuthorDTO]
)
def get_all(db: Session = Depends(get_db)):
    author_service = AuthorService(db)
    return author_service.get_all()


@router.get(
    "/{id}",
    tags=["authors"],
    status_code=status.HTTP_200_OK,
    response_model=Union[ReducedAuthorResponseDTO, AuthorResponseDTO],
    responses={
        status.HTTP_200_OK: {
            "description": "Successful response",
            "content": {
                "application/json": {
                    "schema": {
                        "oneOf": [
                            {"$ref": "#/components/schemas/ReducedAuthorResponseDTO"},
                            {"$ref": "#/components/schemas/AuthorResponseDTO"},
                        ]
                    },
                    "examples": {
                        "Reduced": {
                            "summary": "Reduced response",
                            "value": ReducedAuthorResponseDTO.Config.schema_extra["example"]
                        },
                        "Full": {
                            "summary": "Full response",
                            "value": AuthorResponseDTO.Config.schema_extra["example"]
                        }
                    }   
                }
            }
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Author not found",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Invalid data (validation error)",
        },
    }
)
def get_one(id: int, extended: bool = True, db: Session = Depends(get_db)):
    author_service = AuthorService(db)
    res = author_service.get_by_id(id, extended)
    if res is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
        )
    return res


@router.post(
    "/",
    tags=["authors"],
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
async def create(author: AuthorDTO, db: Session = Depends(get_db)):
    author.validate_ids(db)
    author_service = AuthorService(db)
    try:
        created_author = author_service.create(author)
        return created_author
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
