from sqlalchemy import VARCHAR, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class ExtendedBaseClass(Base):
    __abstract__ = True
    name = mapped_column("name", VARCHAR(63), nullable=False, unique=True)