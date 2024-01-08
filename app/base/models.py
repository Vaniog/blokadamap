from sqlalchemy import VARCHAR, SmallInteger
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, registry
from typing_extensions import Annotated
from sqlalchemy.types import TypeDecorator, CHAR


intpk = Annotated[int, mapped_column(nullable=False, unique=True, primary_key=True, autoincrement=True)]
namestr = Annotated[str, mapped_column(VARCHAR(63), nullable=False)]

class Base(DeclarativeBase):
    type_annotation_map = {
        int: SmallInteger,
        str: VARCHAR(length=63),
    }


class ExtendedBaseClass(Base):
    __abstract__ = True
    name: Mapped[str] = mapped_column(nullable=False, unique=True)