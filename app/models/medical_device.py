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
    medical_device: so.Mapped["MedicalDevice"] = so.relationship(
        "MedicalDevice", back_populates="medical_device_department"
    )
    medical_device_price: so.Mapped[int] = so.mapped_column(unique=True)
    medical_device_state: so.Mapped[str] = so.mapped_column(unique=True)
