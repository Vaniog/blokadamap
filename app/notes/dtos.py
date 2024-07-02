from datetime import date
from typing import List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.authors.models import Author
from app.base.utils import check_id_exists_raise
from app.notes.models import NoteType, Tag, Temporality
from app.point.models import Point


class DiaryDTO(BaseModel):
    # TODO: validate dates (min and max)
    started_at: date  # YYYY-MM-DD
    finished_at: date  # YYYY-MM-DD
    source: str
    author_id: int


class Note2PointDTO(BaseModel):
    point_id: int
    description: str

    def validate_ids(self, db: Session):
        check_id_exists_raise(db, Point, self.point_id)

class NoteDTO(BaseModel):
    author_id: int
    note_type_id: int
    temporality_id: int
    created_at: date  # YYYY-MM-DD
    citation: str
    source: str
    tag_ids: List[int]
    note_to_points: List[Note2PointDTO]

    def validate_ids(self, db: Session):
        check_id_exists_raise(db, Author, self.author_id)
        check_id_exists_raise(db, NoteType, self.note_type_id)
        check_id_exists_raise(db, Temporality, self.temporality_id)
        for tag_id in self.tag_ids:
            check_id_exists_raise(db, Tag, tag_id)
        for note_to_point in self.note_to_points:
            note_to_point.validate_ids(db)

    class Config:
        schema_extra = {
            "example": {
                "author_id": 1,
                "note_type_id": 1,
                "temporality_id": 1,
                "created_at": "1942-08-09",
                "citation": "string",
                "source": "string",
                "tag_ids": [
                    0, 
                ],
                "note_to_points": [
                    {
                    "point_id": 1,
                    "description": "string"
                    }
                ]
            }       
        }

class ReducedNoteDTO(BaseModel):
    author_id: int
    created_at: date
    citation: str

class ReducedNoteResponseDTO(BaseModel):
    note_id: int
    note_info: ReducedNoteDTO

    class Config:
        schema_extra = {
            "example": {
                "note_id": 1,
                "note_info": {
                    "author_id": 1,
                    "created_at": "1942-08-09",
                    "citation": "string"
                }
            }
        }

class TagDTO(BaseModel):
    name: str

class NoteFiltersDTO(BaseModel):
    tag_ids: List[int]
    note_type_id: List[int]
    temporality_id: List[int]

class NoteResponseDTO(BaseModel):
    note_id: int
    note_info: NoteDTO

class BaseResponse(BaseModel):
    description: str