import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db

class UploadedFiles(BaseModel):
    __tablename__ = "uploaded_files"
    user_id: so.Mapped[str] = so.mapped_column(sa.ForeignKey('user.id'),unique=True)
    user: so.Mapped["u.User"] = so.relationship("User", back_populates="uploaded_files")
    file_name: so.Mapped[str] = so.mapped_column(unique=True)
    file_url: so.Mapped[str] = so.mapped_column(unique=True)
    file_type: so.Mapped[str] = so.mapped_column(unique=True)
    file_size: so.Mapped[float] = so.mapped_column(unique=True)