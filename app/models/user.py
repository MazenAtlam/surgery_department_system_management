from datetime import date
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

import app.models as m
from app.models.base_model import BaseModel
from app.utils.password_utils import PasswordMixin


class User(BaseModel, PasswordMixin, UserMixin):
    __tablename__ = "users"

    def __init__(self, password: str, **kwargs):
        """
        Constructor for the Doctor class
        Args:
            passwd (str): Password for the doctor
            **kwargs: Arbitrary keyword arguments
        """
        PasswordMixin.__init__(self, password)
        super().__init__(**kwargs)

    name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False, index=True)
    gender: so.Mapped[str] = so.mapped_column(
        sa.Enum("M", "F", name="gender_enum"), nullable=False
    )
    ssn: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False, index=True)
    dob: so.Mapped[date] = so.mapped_column(sa.Date, nullable=False)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), unique=True, nullable=False, index=True
    )
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    role_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("roles.id"), nullable=False, index=True
    )
    role: so.Mapped["m.Role"] = so.relationship("Role", back_populates="users")
    phone_numbers: so.Mapped[List["m.PhoneNumber"]] = so.relationship(
        "PhoneNumber", back_populates="user"
    )
    pic_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("uploaded_files.id"), nullable=True
    )
    _pic: so.Mapped["m.UploadedFile"] = so.relationship(
        "UploadedFile", back_populates="user", uselist=False
    )
    patients: so.Mapped[List["m.Patient"]] = so.relationship(
        "Patient", back_populates="user", uselist=False
    )
    doctors: so.Mapped[List["m.Doctor"]] = so.relationship(
        "Doctor", back_populates="user", uselist=False
    )
    admins: so.Mapped[List["m.Admin"]] = so.relationship(
        "Admin", back_populates="user", uselist=False
    )

    @hybrid_property
    def pic(self):
        """Returns the user's pic or the default pic if none exists"""
        return self._pic or self.get_default_pic()

    @pic.setter
    def pic(self, value):
        """Setter for the profile picture"""
        self._pic = value

    @classmethod
    def get_default_pic(cls):
        """Returns the default UploadedFile instance for default.png"""
        default_file = m.UploadedFile.query.filter_by(filename="default.png").first()
        if not default_file:
            raise ValueError(
                "Default profile picture 'default.png' not found in database"
            )

        return default_file
