from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Room(BaseModel):
    __tablename__ = "rooms"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    room_location: so.Mapped[str] = so.mapped_column(unique=True, nullable=False)
    medical_devices: so.Mapped[List["m.MedicalDevice"]] = so.relationship(
        "MedicalDevice",
        back_populates="room",  # Must match MedicalDevice's relationship name
        cascade="all, delete-orphan",  # Optional: auto-delete devices if department is deleted
    )
    department_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("departments.id"), nullable=False
    )

    department: so.Mapped["m.Department"] = so.relationship(
        "Department", back_populates="rooms"
    )
    appointments: so.Mapped[List["m.Appointment"]] = so.relationship(
        "Appointment", back_populates="room"
    )
