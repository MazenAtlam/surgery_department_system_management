import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class MedicalDevice(BaseModel):
    __tablename__ = "medical_devices"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    medical_device_name: so.Mapped[str] = so.mapped_column(unique=True)
    department_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("departments.id"))

    department: so.Mapped["m.Department"] = so.relationship(
        "Department", back_populates="medical_devices"
    )
    medical_device_price: so.Mapped[float] = so.mapped_column(unique=True)
    medical_device_state: so.Mapped[str] = so.mapped_column(unique=True)
