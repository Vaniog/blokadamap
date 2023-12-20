from app.base.models import *
from sqlalchemy import Column, ForeignKey, SmallInteger, VARCHAR, Boolean, Text, UniqueConstraint
from geoalchemy2 import Geometry


class Rayon(ExtendedBaseClass):
    __tablename__ = 'rayon'
    rayon_id = Column("rayon_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False)


class Street(ExtendedBaseClass):
    __tablename__ = 'street'
    street_id = Column("street_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False)


class PointType(ExtendedBaseClass):
    __tablename__ = 'point_type'
    point_type_id = Column("point_type_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False)

class PointSubType(ExtendedBaseClass):
    __tablename__ = 'point_subtype'
    point_subtype_id = Column("point_subtype_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    point_type_id = Column("point_type_id", SmallInteger, ForeignKey('point_type.point_type_id'), nullable=False)


class PointSubSubType(ExtendedBaseClass):
    __tablename__ = 'point_subsubtype'
    point_subsubtype_id = Column("point_subsubsubtype_id", SmallInteger, primary_key=True, autoincrement=True, nullable=False)
    point_subtype_id = Column("point_subtype_id", SmallInteger, ForeignKey('point_subtype.point_subtype_id'), nullable=False)

class Point(ExtendedBaseClass):
    __tablename__ = 'point'
    point_id = Column("point_id", SmallInteger, autoincrement=True, primary_key=True, nullable=False)
    rayon_id = Column("rayon_id", SmallInteger, ForeignKey("rayon.rayon_id"))
    street_id = Column("street_id", SmallInteger, ForeignKey("street.street_id"))
    building = Column("building", VARCHAR(15))
    point_subsubtype = Column("point_subsubtype", SmallInteger, ForeignKey('point_subsubtype.point_subsubsubtype_id'), nullable=False)
    is_destroyed = Column("is_destroyed", Boolean, nullable=False)
    has_shelter = Column("has_shelter", Boolean)
    description = Column("description", Text)

    def __init__(self, rayon_id: SmallInteger, street_id: SmallInteger, building: VARCHAR[15], point_subsubtype: SmallInteger, is_destroyed: Boolean, has_shelter: Boolean, name: VARCHAR[63], description: Text):
        super().__init__(name)
        self.rayon_id = rayon_id
        self.street_id = street_id
        self.building = building
        self.point_subsubtype = point_subsubtype
        self.is_destroyed = is_destroyed
        self.has_shelter = has_shelter
        self.description = description

class PointCoordinates(Base):
    __tablename__ = 'point_coordinates'
    point_id = Column("point_id", SmallInteger, ForeignKey("point.point_id"), nullable=False)
    coordinates = Column("coordinates", Geometry('POINT'), nullable=False) #что то решить с координатами
    __table_args__ = (UniqueConstraint('point_id', 'coordinates', name='_point_to_coordinates_uc'),
                      )