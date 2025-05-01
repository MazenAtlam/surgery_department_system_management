from datetime import date

import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from flask_login import UserMixin
from phone_number import PhoneNumber
from role import Role
from uploaded_file import UploadedFile

from app.utils.password_utils import PasswordMixin


class User(BaseModel, PasswordMixin, UserMixin):
    __abstract__ = True

    def __init__(self, password: str, **kwargs):
        """
        Constructor for the Doctor class
        Args:
            passwd (str): Password for the doctor
            **kwargs: Arbitrary keyword arguments
        """
        PasswordMixin.__init__(self, password)
        super().__init__(**kwargs)

    name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    gender: so.Mapped[str] = so.mapped_column(
        sa.Enum("M", "F", name="gender_enum"), nullable=True
    )
    ssn: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    dob: so.Mapped[date] = so.mapped_column(sa.Date)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), unique=True, nullable=False
    )
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    role_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("roles.id"), nullable=False
    )
    role: so.Mapped["Role"] = so.relationship("Role", back_populates="users")
    phone_number_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("phone_numbers.id"), nullable=False
    )
    phone_numbers: so.Mapped["PhoneNumber"] = so.relationship(
        "PhoneNumber", back_populates="users"
    )
    pic_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("uploaded_files.id"), nullable=False
    )
    pic: so.Mapped["UploadedFile"] = so.relationship(
        "UploadedFile", back_populates="users"
    )
