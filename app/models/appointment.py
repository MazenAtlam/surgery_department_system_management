import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Appointment(BaseModel):
    __tablename__ = "appointments"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    patient_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("patients.id"), nullable=False
    )
    patient: so.Mapped["m.Patient"] = so.relationship(
        "Patient", back_populates="appointments"
    )
    doctor_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("doctors.id"), nullable=False
    )
    doctor: so.Mapped["m.Doctor"] = so.relationship(
        "Doctor", back_populates="appointments"
    )
    appointment_date_time: so.Mapped[str] = so.mapped_column(
        sa.DateTime, nullable=False
    )
    room_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("rooms.id"), nullable=True)
    room: so.Mapped["m.Room"] = so.relationship("Room", back_populates="appointments")
    file_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("uploaded_files.id"), nullable=True
    )
    file: so.Mapped["m.UploadedFile"] = so.relationship(
        "UploadedFile", back_populates="appointments"
    )
