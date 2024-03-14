from datetime import date
from enum import Enum

from pydantic import BaseModel


class SexEnum(str, Enum):
    MALE = "M"
    FEMALE = "F"


class Author(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    sex: SexEnum
    birth_date: date  # YYYY-MM-DD
    biography: str
    has_children: bool
    family_status: int
    social_class: int
    nationality: int
    religion: int
    education: int
    occupation: int
    political_party: int
    card: int

    diary_started_at: date  # YYYY-MM-DD
    diary_finished_at: date  # YYYY-MM-DD
    diary_source: str
