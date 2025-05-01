from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class UploadedFile(BaseModel):
    __tablename__ = "uploaded_files"
    user_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey("users.id"))
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="uploaded_files")
    file_name: so.Mapped[str] = so.mapped_column()
    file_url: so.Mapped[str] = so.mapped_column()
    file_type: so.Mapped[str] = so.mapped_column()
    file_size: so.Mapped[float] = so.mapped_column()
    appointments: so.Mapped[List["m.Appointment"]] = so.relationship(
        "Appointment", back_populates="file"
    )
