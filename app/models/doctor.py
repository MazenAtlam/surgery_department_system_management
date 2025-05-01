from datetime import date
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from appointment import Appointment
from base_model import BaseModel
from department import Department
from user import User
from working_slot import WorkingSlot


class Doctor(BaseModel, User):
    __tablename__ = "doctors"

    years_of_experience: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    salary: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    date_of_hire: so.Mapped[date] = so.mapped_column(sa.Date, nullable=False)
    major: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    working_slots: so.Mapped[List["WorkingSlot"]] = so.relationship(
        "WorkingSlot", back_populates="doctor"
    )
    department_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("departments.id"), nullable=False
    )
    department: so.Mapped["Department"] = so.relationship(
        "Department", back_populates="doctors"
    )
    appointments: so.Mapped[List["Appointment"]] = so.relationship(
        "Appointment", back_populates="doctor"
    )
