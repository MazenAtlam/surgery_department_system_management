from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from doctor import Doctor
from medical_device import MedicalDevice
from room import Room

from app import db


class Department(BaseModel):
    __tablename__ = "departments"
    department_name: so.Mapped[str] = so.mapped_column(unique=True)
    department_location: so.Mapped[str] = so.mapped_column(unique=True)
    rooms: so.Mapped[List["Room"]] = so.relationship(
        "Room", back_populates="department", cascade="all, delete-orphan"
    )
    medical_devices: so.Mapped[List["MedicalDevice"]] = so.relationship(
        "MedicalDevice",
        back_populates="department",  # Must match MedicalDevice's relationship name
        cascade="all, delete-orphan",  # Optional: auto-delete devices if department is deleted
    )
    doctors: so.Mapped[List["Doctor"]] = so.relationship(
        "Doctor", back_populates="department", cascade="all, delete-orphan"
    )
