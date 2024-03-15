from pydantic import BaseModel


class PointDto(BaseModel):
    rayon_id: int
    street: str
    building: str
    latitude: float
    longitude: float | None
    point_type: int
    point_subtype: int | None
    point_subsubtype: int | None
    name: str
    description: str


class CoordinatesDto(BaseModel):
    latitude: float
    longitude: float  # TODO: validate coordinates
