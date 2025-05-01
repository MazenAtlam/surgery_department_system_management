from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from appointment import Appointment
from base_model import BaseModel
from dependent import Dependent
from medical_history import MedicalHistory


class Patient(BaseModel):
    __tablename__ = "patients"

    medical_history: so.Mapped[List["MedicalHistory"]] = so.relationship(
        "MedicalHistory", back_populates="patient"
    )
    dependents: so.Mapped[List["Dependent"]] = so.relationship(
        "Dependent", back_populates="patient"
    )
    appointments: so.Mapped[List["Appointment"]] = so.relationship(
        "Appointment", back_populates="patient"
    )
