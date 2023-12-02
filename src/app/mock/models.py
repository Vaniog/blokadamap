from pydantic import BaseModel


class MockModel(BaseModel):
    data: str
