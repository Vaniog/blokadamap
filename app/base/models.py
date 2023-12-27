from sqlalchemy import VARCHAR
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class ExtendedBaseClass(Base):
    __abstract__ = True
    name = mapped_column("name", VARCHAR(63), nullable=False, unique=True)
