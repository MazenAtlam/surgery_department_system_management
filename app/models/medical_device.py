import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db


class MedicalDevices(BaseModel):
    __tablename__ = "medical_devices"
    medical_device_name: so.Mapped[str] = so.mapped_column(unique=True)
    medical_device_department: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("departments.id"), unique=True
    )
    #medical_device: so.Mapped["Department"] = so.relationship(
     #   "Department", back_populates="medical_device"
    #)
    medical_device_price: so.Mapped[float] = so.mapped_column(unique=True)
    medical_device_state: so.Mapped[str] = so.mapped_column(unique=True)
