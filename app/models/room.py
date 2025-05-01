from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from appointment import Appointment
from base_model import BaseModel
from department import Department

from app import db


class Room(BaseModel):
    __tablename__ = "room"
    room_location: so.Mapped[str] = so.mapped_column(unique=True)
    room_device_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("medical_devices.id"), unique=True
    )

    department_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("departments.id"))

    department: so.Mapped["Department"] = so.relationship(
        "Department", back_populates="rooms"
    )
    appointments: so.Mapped[List["Appointment"]] = so.relationship(
        "Appointment", back_populates="room"
    )
