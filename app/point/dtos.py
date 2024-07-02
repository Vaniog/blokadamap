from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

from app.base.utils import check_id_exists_raise
from app.point.models import PointSubSubType, PointSubType, PointType, Rayon


class PointDTO(BaseModel):
    rayon_id: int
    street: str
    building: str
    latitude: float
    longitude: float | None
    point_type_id: int
    point_subtype_id: int | None
    point_subsubtype_id: int | None
    name: str
    description: str | None

    def validate_ids(self, db: Session) -> None:
        check_id_exists_raise(db, Rayon, self.rayon_id)
        check_id_exists_raise(db, PointType, self.point_type_id)
        check_id_exists_raise(db, PointSubType, self.point_subtype_id)
        check_id_exists_raise(db, PointSubSubType, self.point_subsubtype_id)

    class Config:
        schema_extra = {
            "example": {
                "rayon_id": 1,
                "street": "Исаакиевская пл.",
                "building": "4",
                "latitude": 59.56,
                "longitude": 30.18,
                "point_type_id": 1,
                "point_subtype_id": 1,
                "point_subsubtype_id": 1,
                "name": "Исаакиевский собор",
                "description": "Православный собор (ныне музей) с позолоченным куполом и роскошным убранством, построенный в 1818 году",
            }
        }

class ReducedPointDTO(BaseModel):
    point_id: int
    name: str
    has_fixed_coordinates: bool
    has_address: bool

    class Config:
        schema_extra = {
            "example": {
                "point_id": 1,
                "name": "Исаакиевский собор",
                "has_fixed_coordinates": True,
                "has_address": True
            }
        }

class CoordinatesDTO(BaseModel):
    latitude: float
    longitude: float  # TODO: validate coordinates

class PointCoordinatesDTO(BaseModel):
    point_id: int
    coordinates: CoordinatesDTO

class PointFilterDTO(BaseModel):
    type_id: int
    type: str
    are_fixed_coordinates_provided: bool
    is_address_provided: bool
    subtype_id: int | None
    subtype: str
    subsubtype_id: int | None
    subsubtype: str

class PointResponseDTO(BaseModel):
    point_id: int
    point_info: PointDTO

class BaseResponse(BaseModel):
    description: str

class ErrorResponse(BaseModel):
    detail: str
