from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


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
