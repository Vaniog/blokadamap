from sqlalchemy import VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, mapped_column

Base = declarative_base()


class ExtendedBaseClass(DeclarativeBase):
    name = mapped_column("name", VARCHAR(63), nullable=False, unique=True)

    def __init__(self, name: VARCHAR):
        self.name = name
