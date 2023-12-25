from sqlalchemy import (
    CHAR,
    VARCHAR,
    Date,
    ForeignKey,
    SmallInteger,
    Text,
    UniqueConstraint,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import mapped_column
from app.base.models import *


class Many2ManyAuthorsBase(Base):
    __abstract__ = True
    author_id = mapped_column(
        "author_id", SmallInteger, ForeignKey("author.author_id"), nullable=False
    )


# Uniqe models--------------------------------------------------------------------------------------
class Author(Base):
    __tablename__ = "author"
    author_id = mapped_column(
        "author_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False
    )
    first_name = mapped_column("first_name", VARCHAR(63), nullable=False)
    middle_name = mapped_column("middle_name", VARCHAR(63))
    last_name = mapped_column("last_name", VARCHAR(63), nullable=False)
    sex = mapped_column("sex", CHAR(1), nullable=False)
    birth_date = mapped_column("birth_date", Date, nullable=False)
    biography = mapped_column("biography", Text, nullable=False, unique=True)

    def __init__(
        self,
        first_name: VARCHAR,
        middle_name: VARCHAR,
        last_name: VARCHAR,
        sex: CHAR,
        birth_date: Date,
        biography: Text,
    ):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.sex = sex
        self.birth_date = birth_date
        self.biography = biography


class AuthorToPoint(Base):
    __tablename__ = "author_to_point"
    author_id = mapped_column(
        "author_id", SmallInteger, ForeignKey("author.author_id"), nullable=False
    )
    point_id = mapped_column(
        "point_id", SmallInteger, ForeignKey("point.point_id"), nullable=False
    )  # DONT FORGET TO EDIT
    date_start = mapped_column("from", Date, nullable=False)
    date_end = mapped_column("to", Date, nullable=False)
    description = mapped_column("description", Text, nullable=False)
    __table_args__ = (
        UniqueConstraint("author_id", "point_id", name="_author_to_point_uc"),
        PrimaryKeyConstraint('author_id', 'point_id'),
    )

    def __init__(
        self,
        author_id: SmallInteger,
        point_id: SmallInteger,
        date_start: Date,
        date_end: Date,
        description: Text,
    ) -> None:
        self.author_id = author_id
        self.point_id = point_id
        self.date_start = date_start
        self.date_end = date_end
        self.description = description


# ExtendedBaseClass-----------------------------------------------------------------------------------
class FamilyStatus(ExtendedBaseClass):
    __tablename__ = "family_status"
    family_status_id = mapped_column(
        "family_status_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class PoliticalParty(ExtendedBaseClass):
    __tablename__ = "political_party"
    political_party_id = mapped_column(
        "political_party_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class Religion(ExtendedBaseClass):
    __tablename__ = "religion"
    religion_id = mapped_column(
        "religion_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class SocialClass(ExtendedBaseClass):
    __tablename__ = "social_class"
    social_class_id = mapped_column(
        "social_class_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class Nationality(ExtendedBaseClass):
    __tablename__ = "nationality"
    nationality_id = mapped_column(
        "nationality_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class Education(ExtendedBaseClass):
    __tablename__ = "education"
    education_id = mapped_column(
        "education_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class Occupation(ExtendedBaseClass):
    __tablename__ = "occupation"
    occupation_id = mapped_column(
        "occupation_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class Card(ExtendedBaseClass):
    __tablename__ = "card"
    card_id = mapped_column(
        "card_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False
    )


# M2M--------------------------------------------------------------------------------------------------------------------
class Author2FamilyStatus(Many2ManyAuthorsBase):
    __tablename__ = "author_to_family_status"
    family_status_id = mapped_column(
        "family_status_id",
        SmallInteger,
        ForeignKey("family_status.family_status_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint(
            "author_id", "family_status_id", name="_author_to_family_status_id_uc"
        ),
        PrimaryKeyConstraint('author_id', 'family_status_id'),
    )

    def __init__(self, author_id: SmallInteger, family_status_id: SmallInteger):
        self.author_id = author_id
        self.family_status_id = family_status_id


class Author2PoliticalParty(Many2ManyAuthorsBase):
    __tablename__ = "author_to_political_party"
    political_party_id = mapped_column(
        "political_party_id",
        SmallInteger,
        ForeignKey("political_party.political_party_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint(
            "author_id", "political_party_id", name="_author_to_political_party_uc"
        ),
        PrimaryKeyConstraint('author_id', 'political_party_id'),
    )

    def __init__(self, author_id: SmallInteger, political_party_id: SmallInteger):
        self.author_id = author_id
        self.political_party_id = political_party_id


class Author2Religion(Many2ManyAuthorsBase):
    __tablename__ = "author_to_religion_id"
    religion_id = mapped_column(
        "religion_id", SmallInteger, ForeignKey("religion.religion_id"), nullable=False
    )
    __table_args__ = (
        UniqueConstraint(
            "author_id", "religion_id", name="_author_to_political_party_uc"
        ),
        PrimaryKeyConstraint('author_id', 'religion_id'),
    )

    def __init__(self, author_id: SmallInteger, religion_id: SmallInteger):
        self.author_id = author_id
        self.religion_id = religion_id


class Author2SocialClass(Many2ManyAuthorsBase):
    __tablename__ = "author_to_social_class"
    social_class_id = mapped_column(
        "social_class_id",
        SmallInteger,
        ForeignKey("social_class.social_class_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint(
            "author_id", "social_class_id", name="_author_to_social_class_uc"
        ),
        PrimaryKeyConstraint('author_id', 'social_class_id'),
    )

    def __init__(self, author_id: SmallInteger, social_class_id: SmallInteger):
        self.author_id = author_id
        self.social_class_id = social_class_id


class Author2Nationality(Many2ManyAuthorsBase):
    __tablename__ = "author_to_nationality"
    nationality_id = mapped_column(
        "nationality_id",
        SmallInteger,
        ForeignKey("nationality.nationality_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint(
            "author_id", "nationality_id", name="_author_to_nationality_uc"
        ),
        PrimaryKeyConstraint('author_id', 'nationality_id'),
    )

    def __init__(self, author_id: SmallInteger, nationality_id: SmallInteger):
        self.author_id = author_id
        self.nationality_id = nationality_id


class Author2Education(Many2ManyAuthorsBase):
    __tablename__ = "author_to_education"
    education_id = mapped_column(
        "education_id",
        SmallInteger,
        ForeignKey("education.education_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint("author_id", "education_id", name="_author_to_education_uc"),
        PrimaryKeyConstraint('author_id', 'education_id'),
    )

    def __init__(self, author_id: SmallInteger, education_id: SmallInteger):
        self.author_id = author_id
        self.education_id = education_id


class Author2Occupation(Many2ManyAuthorsBase):
    __tablename__ = "author_to_occupation_id"
    occupation_id = mapped_column(
        "occupation_id",
        SmallInteger,
        ForeignKey("occupation.occupation_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint("author_id", "occupation_id", name="_author_to_occupation_uc"),
        PrimaryKeyConstraint('author_id', 'occupation_id'),
    )

    def __init__(self, author_id: SmallInteger, occupation_id: SmallInteger):
        self.author_id = author_id
        self.occupation_id = occupation_id


class Author2Card(Many2ManyAuthorsBase):
    __tablename__ = "author_to_card_id"
    card_id = mapped_column(
        "card_id", SmallInteger, ForeignKey("card.card_id"), nullable=False
    )
    __table_args__ = (
        UniqueConstraint("author_id", "card_id", name="_author_to_card_uc"),
        PrimaryKeyConstraint('author_id', 'card_id'),
    )

    def __init__(self, author_id: SmallInteger, card_id: SmallInteger):
        self.author_id = author_id
        self.card_id = card_id
