from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Room(BaseModel):
    __tablename__ = "room"
    room_location: so.Mapped[str] = so.mapped_column(unique=True)
    room_device_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("medical_devices.id"), unique=True
    )

    department_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("departments.id"))

    department: so.Mapped["m.Department"] = so.relationship(
        "Department", back_populates="rooms"
    )
    appointments: so.Mapped[List["m.Appointment"]] = so.relationship(
        "Appointment", back_populates="room"
    )
