from geoalchemy2 import Geography
from sqlalchemy import (
    VARCHAR,
    Boolean,
    ForeignKey,
    SmallInteger,
    Text,
    UniqueConstraint,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.base.models import *
from app.authors.models import Author2Point
from app.notes.models import NoteToPoint


class Rayon(ExtendedBaseClass):
    __tablename__ = "rayon"
    rayon_id = mapped_column(
        "rayon_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False
    )


class Street(ExtendedBaseClass):
    __tablename__ = "street"
    street_id = mapped_column(
        "street_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False
    )


class PointType(ExtendedBaseClass):
    __tablename__ = "point_type"
    point_type_id = mapped_column(
        "point_type_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )


class PointSubType(ExtendedBaseClass):
    __tablename__ = "point_subtype"
    point_subtype_id = mapped_column(
        "point_subtype_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    point_type_id = mapped_column(
        "point_type_id",
        SmallInteger,
        ForeignKey("point_type.point_type_id"),
        nullable=False,
    )
    point_type = relationship("PointType", back_populates="point_subtype")


class PointSubSubType(ExtendedBaseClass):
    __tablename__ = "point_subsubtype"
    point_subsubtype_id = mapped_column(
        "point_subsubsubtype_id",
        SmallInteger,
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )
    point_subtype_id = mapped_column(
        "point_subtype_id",
        SmallInteger,
        ForeignKey("point_subtype.point_subtype_id"),
        nullable=False,
    )
    point_subtype = relationship("PointSubType", back_populates="point_subsubtype")


class Point(ExtendedBaseClass):
    __tablename__ = "point"
    point_id = mapped_column(
        "point_id", SmallInteger, autoincrement=True, primary_key=True, nullable=False
    )
    rayon_id = mapped_column("rayon_id", SmallInteger, ForeignKey("rayon.rayon_id"))
    street_id = mapped_column("street_id", SmallInteger, ForeignKey("street.street_id"))
    building = mapped_column("building", VARCHAR(15))
    point_subsubtype = mapped_column(
        "point_subsubtype",
        SmallInteger,
        ForeignKey("point_subsubtype.point_subsubsubtype_id"),
        nullable=False,
    )
    is_destroyed = mapped_column("is_destroyed", Boolean, nullable=False)
    has_shelter = mapped_column("has_shelter", Boolean)
    description = mapped_column("description", Text)

    rayon = relationship("Rayon", back_populates="point")
    street = relationship("Street", back_populates="point")
    point_subsubtype = relationship("PointSubSubType", back_populates="point")
    author = relationship('Author', secondary=Author2Point, back_populates='point')
    notes = relationship("Note", secondary=NoteToPoint, back_populates="point")



# class PointCoordinates(Base):
#     __tablename__ = "point_coordinates"
#     point_id = mapped_column(
#         "point_id", SmallInteger, ForeignKey("point.point_id"), nullable=False
#     )
#     coordinates = mapped_column(
#         "coordinates", Geography(geometry_type='POINT'), nullable=False
#     )
#     __table_args__ = (
#         UniqueConstraint("point_id", "coordinates", name="_point_to_coordinates_uc"),
#         PrimaryKeyConstraint('point_id'),
#     )
#     point = relationship("Point", back_populates="point_coordinates")
