from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR

Base = declarative_base()


class ExtendedBaseClass(Base):
    name = Column("name", VARCHAR(63), nullable=False, unique=True)

    def __init__(self, name: VARCHAR[63]):
        self.name = name
