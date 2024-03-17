from datetime import date
from typing import List

from pydantic import BaseModel


class DiaryDto(BaseModel):
    # TODO: validate dates (min and max)
    started_at: date  # YYYY-MM-DD
    finished_at: date  # YYYY-MM-DD
    source: str
    author: int


class NoteDto(BaseModel):
    author: int
    note_type: int
    temporality: int
    created_at: date  # YYYY-MM-DD
    citation: str
    source: str
    tags: List[int]
    point: int


class TagDto(BaseModel):
    name: str
