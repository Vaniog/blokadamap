from sqlalchemy import String, Text, ForeignKey, Table, Column, Date
import datetime
from app.base.models import *
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


author2political_party = Table(
    "author_to_political_party",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("political_party_id", ForeignKey("political_party.political_party_id"), primary_key=True),
)

author2religion = Table(
    "author_to_religion",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("religion_id", ForeignKey("religion.religion_id"), primary_key=True),
)

author2social_class = Table(
    "author_to_social_class",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("social_class_id", ForeignKey("social_class.social_class_id"), primary_key=True),
)

author2nationality = Table(
    "author_to_nationality",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("nationality_id", ForeignKey("nationality.nationality_id"), primary_key=True),
)

author2education = Table(
    "author_to_education",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("education_id", ForeignKey("education.education_id"), primary_key=True),
)

author2occupation = Table(
    "author_to_occupation",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("occupation_id", ForeignKey("occupation.occupation_id"), primary_key=True),
)

author2card = Table(
    "author_to_card",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("card_id", ForeignKey("card.card_id"), primary_key=True),
)

author2point = Table(
    "author_to_point",
    Base.metadata,
    Column("author_id", ForeignKey("author.author_id"), primary_key=True),
    Column("point_id", ForeignKey("point.point_id"), primary_key=True),
    Column("from", Date, nullable=False),
    Column("to", Date, nullable=False),
    Column("description", Text, nullable=False)
)

class Author(Base):
    __tablename__ = 'author'
    author_id: Mapped[intpk]
    first_name: Mapped[namestr]
    middle_name: Mapped[namestr] = mapped_column(nullable=True)
    last_name: Mapped[namestr]
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    birth_date: Mapped[datetime.date] = mapped_column(nullable=False)
    family_status_id: Mapped[int] = mapped_column(ForeignKey("family_status.family_status_id"))
    has_children: Mapped[bool] = mapped_column(nullable=False)
    biography: Mapped[str] = mapped_column(Text, nullable=False, unique=True)

    family_status: Mapped["FamilyStatus"] = relationship(back_populates="authors")
    diaries: Mapped[List["Diary"]] = relationship(back_populates="author")
    political_parties: Mapped[List["PoliticalParty"]] = relationship(secondary=author2political_party, back_populates="authors")
    religions: Mapped[List["Religion"]] = relationship(secondary=author2religion, back_populates="authors")
    social_classes: Mapped[List["SocialClass"]] = relationship(secondary=author2social_class, back_populates="authors")
    nationalities: Mapped[List["Nationality"]] = relationship(secondary=author2nationality, back_populates="authors")
    education: Mapped[List["Education"]] = relationship(secondary=author2education, back_populates="authors")
    occupation: Mapped[List["Occupation"]] = relationship(secondary=author2occupation, back_populates="authors")
    cards: Mapped[List["Card"]] = relationship(secondary=author2card, back_populates="authors")
    points: Mapped[List["Point"]] = relationship(secondary=author2point, back_populates="authors")


class FamilyStatus(ExtendedBaseClass):
    __tablename__ = 'family_status'
    family_status_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(back_populates="family_status")


class PoliticalParty(ExtendedBaseClass):
    __tablename__ = 'political_party'
    political_party_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2political_party,
                                                                     back_populates="political_parties")


class Religion(ExtendedBaseClass):
    __tablename__ = 'religion'
    religion_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2religion,
                                                   back_populates="religions")


class SocialClass(ExtendedBaseClass):
    __tablename__ = 'social_class'
    social_class_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2social_class,
                                                   back_populates="social_classes")


class Nationality(ExtendedBaseClass):
    __tablename__ = 'nationality'
    nationality_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2nationality,
                                                   back_populates="nationalities")

class Education(ExtendedBaseClass):
    __tablename__ = 'education'
    education_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2education,
                                                   back_populates="education")


class Occupation(ExtendedBaseClass):
    __tablename__ = 'occupation'
    occupation_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2occupation,
                                                   back_populates="occupation")


class Card(ExtendedBaseClass):
    __tablename__ = 'card'
    card_id: Mapped[intpk]
    authors: Mapped[List["Author"]] = relationship(secondary=author2card,
                                                   back_populates="cards")


