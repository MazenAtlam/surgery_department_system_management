import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from department import Department

from app import db


class MedicalDevice(BaseModel):
    __tablename__ = "medical_devices"
    medical_device_name: so.Mapped[str] = so.mapped_column(unique=True)
    department_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("departments.id"))

    department: so.Mapped["Department"] = so.relationship(
        "Department", back_populates="medical_devices"
    )
    medical_device_price: so.Mapped[float] = so.mapped_column(unique=True)
    medical_device_state: so.Mapped[str] = so.mapped_column(unique=True)
