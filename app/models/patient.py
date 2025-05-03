from enum import Enum
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class BloodType(str, Enum):
    A_POS = "A+"
    A_NEG = "A-"
    B_POS = "B+"
    B_NEG = "B-"
    AB_POS = "AB+"
    AB_NEG = "AB-"
    O_POS = "O+"
    O_NEG = "O-"


class Patient(BaseModel):
    __abstract__ = False
    __tablename__ = "patients"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    medical_history: so.Mapped[List["m.MedicalHistory"]] = so.relationship(
        "MedicalHistory", back_populates="patient"
    )
    dependents: so.Mapped[List["m.Dependent"]] = so.relationship(
        "Dependent", back_populates="patient"
    )
    appointments: so.Mapped[List["m.Appointment"]] = so.relationship(
        "Appointment", back_populates="patient"
    )
    blood_type: so.Mapped[BloodType] = so.mapped_column(
        sa.Enum(BloodType), index=True, nullable=True
    )

    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False, unique=True
    )
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="patient")
