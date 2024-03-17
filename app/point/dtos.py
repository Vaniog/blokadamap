from pydantic import BaseModel


class PointDto(BaseModel):
    rayon_id: int
    street: str
    building: str
    latitude: float
    longitude: float | None
    point_type_id: int
    point_subtype_id: int | None
    point_subsubtype_id: int | None
    name: str
    description: str


class CoordinatesDto(BaseModel):
    latitude: float
    longitude: float  # TODO: validate coordinates
