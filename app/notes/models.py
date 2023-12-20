from sqlalchemy import Date, ForeignKey, SmallInteger, Text, UniqueConstraint
from sqlalchemy.orm import mapped_column
from app.base.models import *


class Diary(Base):
    __tablename__ = "diary"
    diary_id = mapped_column(
        "diary_id", SmallInteger, primary_key=True, nullable=False, autoincrement=True
    )
    author_id = mapped_column(
        "author_id", SmallInteger, ForeignKey("author.author_id"), nullable=False
    )
    started_at = mapped_column("started_at", Date, nullable=False)
    finished_at = mapped_column("finished_at", Date, nullable=False)
    name = mapped_column("name", Text, nullable=False)
    storage = mapped_column("storage", Text)

    def __init__(
        self,
        diary_id: SmallInteger,
        author_id: SmallInteger,
        started_at: Date,
        finished_at: Date,
        name: Text,
        storage: Text,
    ):
        self.diary_id = diary_id
        self.author_id = author_id
        self.started_at = started_at
        self.finished_at = finished_at
        self.name = name
        self.storage = storage


class Note(Base):
    __tablename__ = "note"
    note_id = mapped_column(
        "note_id", SmallInteger, primary_key=True, nullable=False, autoincrement=True
    )
    diary_id = mapped_column(
        "diary_id", SmallInteger, ForeignKey("diary.diary_id"), nullable=False
    )
    point_id = mapped_column(
        "point_id", SmallInteger, ForeignKey("point.point_id"), nullable=False
    )
    created_at = mapped_column("created_at", Date, nullable=False)
    citation = mapped_column("citation", Text, nullable=False)

    def __init__(
        self,
        diary_id: SmallInteger,
        point_id: SmallInteger,
        created_at: Date,
        citation: Text,
    ):
        self.diary_id = diary_id
        self.point_id = point_id
        self.created_at = created_at
        self.citation = citation


class EventTag(ExtendedBaseClass):
    __tablename__ = "event_tag"
    event_tag_id = mapped_column(
        "event_tag_id",
        SmallInteger,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )


class EventType(ExtendedBaseClass):
    __tablename__ = "event_type"
    event_type_id = mapped_column(
        "event_type_id",
        SmallInteger,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )


class EventTemporality(ExtendedBaseClass):
    __tablename__ = "event_temporality"
    event_temporality_id = mapped_column(
        "event_temporality_id",
        SmallInteger,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )


class EventName(ExtendedBaseClass):
    __tablename__ = "event_name"
    event_name_id = mapped_column(
        "event_name_id",
        SmallInteger,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )


class EventSource(ExtendedBaseClass):
    __tablename__ = "event_source"
    event_source_id = mapped_column(
        "event_source_id",
        SmallInteger,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )


class Event(Base):
    __tablename__ = "event"
    note_id = mapped_column(
        "note_id",
        SmallInteger,
        ForeignKey("note.note_id"),
        primary_key=True,
        nullable=False,
    )
    event_type_id = mapped_column(
        "event_type_id",
        SmallInteger,
        ForeignKey("event_type.event_type_id"),
        nullable=False,
    )
    happened_at = mapped_column("happened_at", Date, nullable=False)
    event_temporality_id = mapped_column(
        "event_temporality_id",
        SmallInteger,
        ForeignKey("event_temporality.event_temporality_id"),
        nullable=False,
    )
    event_name_id = mapped_column(
        "event_name_id", SmallInteger, ForeignKey("event_name.event_name_id")
    )
    event_source_id = mapped_column(
        "event_source_id",
        SmallInteger,
        ForeignKey("event_source.event_source_id"),
        nullable=False,
    )

    def __init__(
        self,
        note_id,
        event_type_id,
        happened_at,
        event_temporality_id,
        event_name_id,
        event_source_id,
    ):
        self.note_id = note_id
        self.event_type_id = event_type_id
        self.happened_at = happened_at
        self.event_temporality_id = event_temporality_id
        self.event_name = event_name_id
        self.event_source_id = event_source_id


class Event2EventTag(Base):
    __tablename__ = "event_to_event_tag"
    event_id = mapped_column(
        "event_id", SmallInteger, ForeignKey("event.note_id"), nullable=False
    )
    event_tag_id = mapped_column(
        "event_tag_id",
        SmallInteger,
        ForeignKey("event_tag.event_tag_id"),
        nullable=False,
    )
    __table_args__ = (
        UniqueConstraint("event_id", "event_tag_id", name="_event_to_tag_uc"),
    )

    def __init__(self, event_id: SmallInteger, event_tag_id: SmallInteger):
        self.event_id = event_id
        self.event_tag_id = event_tag_id
