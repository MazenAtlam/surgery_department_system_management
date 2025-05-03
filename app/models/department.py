from typing import List

import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Department(BaseModel):
    __tablename__ = "departments"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    department_name: so.Mapped[str] = so.mapped_column(unique=True, nullable=False)
    department_location: so.Mapped[str] = so.mapped_column(nullable=False)
    rooms: so.Mapped[List["m.Room"]] = so.relationship(
        "Room", back_populates="department", cascade="all, delete-orphan"
    )
    doctors: so.Mapped[List["m.Doctor"]] = so.relationship(
        "Doctor", back_populates="department", cascade="all, delete-orphan"
    )
