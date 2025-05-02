from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class UploadedFile(BaseModel):
    __tablename__ = "uploaded_files"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    user: so.Mapped["m.User"] = so.relationship(
        "User", back_populates="_pic", uselist=False
    )
    file_name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    file_url: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    file_type: so.Mapped[str] = so.mapped_column(sa.String(10), nullable=False)
    file_size: so.Mapped[float] = so.mapped_column(sa.Float, nullable=False)
    appointments: so.Mapped[List["m.Appointment"]] = so.relationship(
        "Appointment", back_populates="file"
    )
