from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from appointment import Appointment
from base_model import BaseModel
from user import User

from app import db


class UploadedFile(BaseModel):
    __tablename__ = "uploaded_files"
    user_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("user.id"))
    user: so.Mapped["User"] = so.relationship("User", back_populates="uploaded_files")
    file_name: so.Mapped[str] = so.mapped_column()
    file_url: so.Mapped[str] = so.mapped_column()
    file_type: so.Mapped[str] = so.mapped_column()
    file_size: so.Mapped[float] = so.mapped_column()
    appointments: so.Mapped[List["Appointment"]] = so.relationship(
        "Appointment", back_populates="file"
    )
