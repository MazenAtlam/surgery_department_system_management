import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db
from doctor import Doctor
from patient import Patient
from uploaded_file import UploadedFile
from room import Room
class Appointment(BaseModel):
    __tablename__ = "appointments"
    patient_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("patients.id"),)
    doctor_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("doctors.id"))
    appointment_date_time: so.Mapped[str] = so.mapped_column(sa.DateTime)
    room_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("room.id"))
    file_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("uploaded_files.id"))
    patient: so.Mapped["Patient"] = so.relationship("Patient", back_populates="appointments")
    doctor: so.Mapped["Doctor"] = so.relationship("Doctor", back_populates="appointments")
    room: so.Mapped["Room"] = so.relationship("Room", back_populates="appointments")
    file: so.Mapped["UploadedFile"] = so.relationship("UploadedFile", back_populates="appointments")
