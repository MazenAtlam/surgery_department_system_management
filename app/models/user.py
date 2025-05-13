from datetime import date
from typing import List, Optional

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
        relationship_fields = [
            "role",
            "_pic",
            "phone_numbers",
            "patients",
            "doctors",
            "admins",
        ]
        model_kwargs = {k: v for k, v in kwargs.items() if k not in relationship_fields}
        super().__init__(**model_kwargs)

        PasswordMixin.__init__(self, password)

        for field in relationship_fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])

    username: so.Mapped[str] = so.mapped_column(
        sa.String(100), nullable=False, index=True
    )
    gender: so.Mapped[str] = so.mapped_column(
        sa.Enum("M", "F", name="gender_enum"), nullable=False
    )
    ssn: so.Mapped[str] = so.mapped_column(sa.String(14), nullable=False, index=True)
    date_of_birth: so.Mapped[date] = so.mapped_column(sa.Date, nullable=False)
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
        sa.ForeignKey("uploaded_files.id"), nullable=False
    )
    _pic: so.Mapped["m.UploadedFile"] = so.relationship(
        "UploadedFile", back_populates="user", uselist=False, foreign_keys=[pic_id]
    )
    patient: so.Mapped[Optional["m.Patient"]] = so.relationship(
        "Patient", back_populates="user", uselist=False
    )
    doctor: so.Mapped[Optional["m.Doctor"]] = so.relationship(
        "Doctor", back_populates="user", uselist=False
    )
    admin: so.Mapped[Optional["m.Admin"]] = so.relationship(
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
