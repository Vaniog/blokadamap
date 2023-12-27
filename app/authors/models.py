from sqlalchemy import (
    CHAR,
    VARCHAR,
    Column,
    Date,
    ForeignKey,
    SmallInteger,
    Table,
    Text,
)
from sqlalchemy.orm import mapped_column, relationship

from app.base.models import *

# M2M-------------------------------------------------------------------------------------------

Author2FamilyStatus = Table(
    "author_to_family_status",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "family_status_id",
        SmallInteger,
        ForeignKey("family_status.family_status_id"),
        primary_key=True,
        nullable=False,
    ),
)


Author2Religion = Table(
    "author_to_religion",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "religion_id",
        SmallInteger,
        ForeignKey("religion.religion_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2PoliticalParty = Table(
    "author_to_political_party",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "political_party_id",
        SmallInteger,
        ForeignKey("political_party.political_party_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2SocialClass = Table(
    "author_to_social_class",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "social_class_id",
        SmallInteger,
        ForeignKey("social_class.social_class_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2Nationality = Table(
    "author_to_nationality",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "nationality_id",
        SmallInteger,
        ForeignKey("nationality.nationality_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2Education = Table(
    "author_to_education",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "education_id",
        SmallInteger,
        ForeignKey("education.education_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2Occupation = Table(
    "author_to_occupation",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "occupation_id",
        SmallInteger,
        ForeignKey("occupation.occupation_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2Card = Table(
    "author_to_card",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "card_id",
        SmallInteger,
        ForeignKey("card.card_id"),
        primary_key=True,
        nullable=False,
    ),
)

Author2Point = Table(
    "author_to_point",
    Base.metadata,
    Column(
        "author_id",
        SmallInteger,
        ForeignKey("author.author_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "point_id",
        SmallInteger,
        ForeignKey("point.point_id"),
        primary_key=True,
        nullable=False,
    ),
    Column("from", Date, nullable=False),
    Column("to", Date, nullable=False),
    Column("description", Text, nullable=False),
)


# Uniqe models--------------------------------------------------------------------------------------
class Author(Base):
    __tablename__ = "author"
    author_id = mapped_column(SmallInteger, primary_key=True, nullable=False)
    first_name = mapped_column(VARCHAR(63), nullable=False)
    middle_name = mapped_column(VARCHAR(63))
    last_name = mapped_column(VARCHAR(63), nullable=False)
    sex = mapped_column(CHAR(1), nullable=False)
    birth_date = mapped_column(Date, nullable=False)
    biography = mapped_column(Text, nullable=False, unique=True)

    family_status = relationship(
        "FamilyStatus", secondary=Author2FamilyStatus, back_populates="author"
    )
    religion = relationship(
        "Religion", secondary=Author2Religion, back_populates="author"
    )
    political_party = relationship(
        "PoliticalParty", secondary=Author2PoliticalParty, back_populates="author"
    )
    social_classes = relationship(
        "SocialClass", secondary=Author2SocialClass, back_populates="author"
    )
    nationality = relationship(
        "Nationality", secondary=Author2Nationality, back_populates="author"
    )
    education = relationship(
        "Education", secondary=Author2Education, back_populates="author"
    )
    occupation = relationship(
        "Occupation", secondary=Author2Occupation, back_populates="author"
    )
    card = relationship("Card", secondary=Author2Card, back_populates="author")
    point = relationship("Point", secondary=Author2Point, back_populates="author")


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

    authors = relationship(
        "Author", secondary=Author2FamilyStatus, back_populates="family_status"
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
    authors = relationship(
        "Author", secondary=Author2PoliticalParty, back_populates="family_status"
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
    authors = relationship(
        "Author", secondary=Author2Religion, back_populates="religion"
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

    authors = relationship(
        "Author", secondary=Author2SocialClass, back_populates="social_class"
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
    authors = relationship(
        "Author", secondary=Author2Nationality, back_populates="nationality"
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
    authors = relationship(
        "Author", secondary=Author2Education, back_populates="education"
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
    authors = relationship(
        "Author", secondary=Author2Occupation, back_populates="occupation"
    )


class Card(ExtendedBaseClass):
    __tablename__ = "card"
    card_id = mapped_column(
        "card_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False
    )
    authors = relationship("Author", secondary=Author2Card, back_populates="card")


def init():
    pass
