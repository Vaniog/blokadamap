from datetime import date
from typing import List

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.authors.models import Author
from app.base.utils import check_id_exists_raise
from app.notes.models import NoteType, Tag, Temporality
from app.point.models import Point


class DiaryDto(BaseModel):
    # TODO: validate dates (min and max)
    started_at: date  # YYYY-MM-DD
    finished_at: date  # YYYY-MM-DD
    source: str
    author_id: int


class NoteDto(BaseModel):
    author_id: int
    note_type_id: int
    temporality_id: int
    created_at: date  # YYYY-MM-DD
    citation: str
    source: str
    tag_ids: List[int]
    point_id: int

    def validate_ids(self, db: Session):
        check_id_exists_raise(db, Author, self.author_id)
        check_id_exists_raise(db, NoteType, self.note_type_id)
        check_id_exists_raise(db, Temporality, self.temporality_id)
        for tag_id in self.tag_ids:
            check_id_exists_raise(db, Tag, tag_id)
        check_id_exists_raise(db, Point, self.point_id)
        return 1


class TagDto(BaseModel):
    name: str
