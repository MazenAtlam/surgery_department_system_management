import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db

class Room(BaseModel):
    __tablename__ = "room"
    room_location: so.Mapped[str] = so.mapped_column(unique=True)
    room_device_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey('medical_devices.id'),unique=True)
    room_device: so.Mapped["m.MedicalDevice"] = so.relationship("MedicalDevice", back_populates="room_device")
    room_department_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey('departments.id'),unique=True)
    room_department: so.Mapped["d.Department"] = so.relationship("Department", back_populates="room_department")