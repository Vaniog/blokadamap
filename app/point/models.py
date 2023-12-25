from geoalchemy2 import Geometry
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
from app.base.models import *


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

    def __init__(
        self,
        rayon_id: SmallInteger,
        street_id: SmallInteger,
        building: VARCHAR,
        point_subsubtype: SmallInteger,
        is_destroyed: Boolean,
        has_shelter: Boolean,
        name: VARCHAR,
        description: Text,
    ):
        super().__init__(name)
        self.rayon_id = rayon_id
        self.street_id = street_id
        self.building = building
        self.point_subsubtype = point_subsubtype
        self.is_destroyed = is_destroyed
        self.has_shelter = has_shelter
        self.description = description


class PointCoordinates(Base):
    __tablename__ = "point_coordinates"
    point_id = mapped_column(
        "point_id", SmallInteger, ForeignKey("point.point_id"), nullable=False
    )
    coordinates = mapped_column(
        "coordinates", Geometry("POINT"), nullable=False
    )  # что то решить с координатами
    __table_args__ = (
        UniqueConstraint("point_id", "coordinates", name="_point_to_coordinates_uc"),
        PrimaryKeyConstraint('point_id'),
    )
