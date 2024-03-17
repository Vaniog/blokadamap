from datetime import date
from typing import List

from pydantic import BaseModel


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


class TagDto(BaseModel):
    name: str
