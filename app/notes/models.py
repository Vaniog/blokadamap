from sqlalchemy import String, Text, ForeignKey, Table, Column
import datetime
from app.base.models import *
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


note2tag = Table(
    "note_to_tag",
    Base.metadata,
    Column("note_id", ForeignKey("note.note_id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.tag_id"), primary_key=True),
)

note2point = Table(
    "note_to_point",
    Base.metadata,
    Column("note_id", ForeignKey("note.note_id"), primary_key=True),
    Column("point_id", ForeignKey("point.point_id"), primary_key=True),
    Column("description", Text, nullable=False)
)


class Note(Base):
    __tablename__ = 'note'
    note_id: Mapped[intpk]
    diary_id: Mapped[int] = mapped_column(ForeignKey("diary.diary_id"))
    note_type_id: Mapped[int] = mapped_column(ForeignKey("note_type.note_type_id"))
    temporality_id: Mapped[int] = mapped_column(ForeignKey("temporality.temporality_id"))
    created_at: Mapped[datetime.date] = mapped_column(nullable=False)
    citation: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    source: Mapped[str] = mapped_column(nullable=False)

    note_type: Mapped["NoteType"] = relationship(back_populates="notes")
    temporality: Mapped["Temporality"] = relationship(back_populates="notes")
    diary: Mapped["Diary"] = relationship(back_populates="notes")
    tags: Mapped[List["Tag"]] = relationship(secondary=note2tag, back_populates="notes")
    points: Mapped[List["Point"]] = relationship(secondary=note2point, back_populates="notes")


class Diary(Base):
    __tablename__ = 'diary'
    diary_id: Mapped[intpk]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.author_id"))
    started_at: Mapped[datetime.date] = mapped_column(nullable=False)
    finished_at: Mapped[datetime.date] = mapped_column(nullable=False)
    source: Mapped[str] = mapped_column(Text)

    author: Mapped["Author"] = relationship(back_populates="diaries")
    notes: Mapped[List["Note"]] = relationship(back_populates="diary")


class Tag(ExtendedBaseClass):
    __tablename__ = 'tag'
    tag_id: Mapped[intpk]
    notes: Mapped[List["Note"]] = relationship(secondary=note2tag,
                                                   back_populates="tags")


class NoteType(ExtendedBaseClass):
    __tablename__ = 'note_type'
    note_type_id: Mapped[intpk]
    notes: Mapped[List["Note"]] = relationship(back_populates="note_type")


class Temporality(ExtendedBaseClass):
    __tablename__ = 'temporality'
    temporality_id: Mapped[intpk]
    notes: Mapped[List["Note"]] = relationship(back_populates="temporality")


