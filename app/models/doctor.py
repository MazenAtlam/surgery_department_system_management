from datetime import date
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Doctor(BaseModel):
    __abstract__ = False
    __tablename__ = "doctors"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    years_of_experience: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    salary: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    date_of_hire: so.Mapped[date] = so.mapped_column(sa.Date, nullable=False)
    major: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    working_slots: so.Mapped[List["m.WorkingSlot"]] = so.relationship(
        "WorkingSlot", back_populates="doctor"
    )
    department_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("departments.id"), nullable=False
    )
    department: so.Mapped["m.Department"] = so.relationship(
        "Department", back_populates="doctors"
    )
    appointments: so.Mapped[List["m.Appointment"]] = so.relationship(
        "Appointment", back_populates="doctor"
    )
    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False, unique=True
    )
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="doctor")
