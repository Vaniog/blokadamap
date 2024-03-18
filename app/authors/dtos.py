from datetime import date
from enum import Enum

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.authors.models import (
    Card,
    Education,
    FamilyStatus,
    Nationality,
    Occupation,
    PoliticalParty,
    Religion,
    SocialClass,
)
from app.base.utils import check_id_exists_raise


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

    def validate_ids(self, db: Session) -> None:
        check_id_exists_raise(db, FamilyStatus, self.family_status_id)
        check_id_exists_raise(db, SocialClass, self.social_class_id)
        check_id_exists_raise(db, Nationality, self.nationality_id)
        check_id_exists_raise(db, Religion, self.religion_id)
        check_id_exists_raise(db, Education, self.education_id)
        check_id_exists_raise(db, Occupation, self.occupation_id)
        check_id_exists_raise(db, PoliticalParty, self.political_party_id)
        check_id_exists_raise(db, Card, self.card_id)
