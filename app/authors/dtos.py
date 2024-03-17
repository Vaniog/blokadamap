from datetime import date
from enum import Enum

from pydantic import BaseModel


class SexEnum(str, Enum):
    MALE = "M"
    FEMALE = "F"


class AuthorDto(BaseModel):
    last_name: str
    first_name: str
    middle_name: str
    sex: SexEnum
    birth_date: date  # YYYY-MM-DD
    biography: str
    has_children: bool
    family_status_id: int
    social_class_id: int
    nationality_id: int
    religion_id: int
    education_id: int
    occupation_id: int
    political_party_id: int
    card_id: int

    diary_started_at: date  # YYYY-MM-DD
    diary_finished_at: date  # YYYY-MM-DD
    diary_source: str
