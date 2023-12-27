from sqlalchemy import Column, Date, ForeignKey, SmallInteger, Table, Text
from sqlalchemy.orm import mapped_column, relationship

from app.base.models import *


class Diary(Base):
    __tablename__ = "diary"

    diary_id = mapped_column(SmallInteger, primary_key=True, nullable=False)
    author_id = mapped_column(
        SmallInteger, ForeignKey("author.author_id"), unique=True, nullable=False
    )
    started_at = mapped_column(Date, nullable=False)
    finished_at = mapped_column(Date, nullable=False)
    sources = mapped_column(Text, nullable=False)

    author = relationship("Author", back_populates="diary", uselist=False)


NoteToTag = Table(
    "note_to_tag",
    Base.metadata,
    Column(
        "note_id",
        SmallInteger,
        ForeignKey("note.note_id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "tag_id",
        SmallInteger,
        ForeignKey("tag.tag_id"),
        primary_key=True,
        nullable=False,
    ),
)

NoteToPoint = Table(
    "note_to_point",
    Base.metadata,
    Column(
        "note_id",
        SmallInteger,
        ForeignKey("note.note_id"),
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
    Column("description", Text, nullable=False),
)


class NoteType(ExtendedBaseClass):
    __tablename__ = "note_type"
    note_type_id = mapped_column(SmallInteger, primary_key=True, nullable=False)


class Temporality(ExtendedBaseClass):
    __tablename__ = "temporality"
    temporality_id = mapped_column(SmallInteger, primary_key=True, nullable=False)


class Tag(ExtendedBaseClass):
    __tablename__ = "tag"
    tag_id = Column(SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    notes = relationship("Note", secondary=NoteToTag, back_populates="tag")


class Note(Base):
    __tablename__ = "note"
    note_id = mapped_column(SmallInteger, primary_key=True, nullable=False)
    diary_id = mapped_column(SmallInteger, ForeignKey("diary.diary_id"), nullable=False)
    note_type_id = mapped_column(
        SmallInteger, ForeignKey("note_type.note_type_id"), nullable=False
    )
    temporality_id = mapped_column(
        SmallInteger, ForeignKey("temporality.temporality_id"), nullable=False
    )
    created_at = mapped_column(Date, nullable=False)
    citation = mapped_column(Text, nullable=False, unique=True)
    sources = mapped_column(Text, nullable=False)

    diary = relationship("Diary", back_populates="note")
    note_type = relationship("NoteType", back_populates="note")
    temporality = relationship("Temporality", back_populates="note")
    tags = relationship("Tag", secondary=NoteToTag, back_populates="note")
    point = relationship("Point", secondary=NoteToPoint, back_populates="note")


def init():
    pass
