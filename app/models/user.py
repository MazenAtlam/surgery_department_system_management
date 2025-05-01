from datetime import date
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from flask_login import UserMixin
from phone_number import PhoneNumber
from role import Role
from sqlalchemy.ext.hybrid import hybrid_property
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

    name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False, index=True)
    gender: so.Mapped[str] = so.mapped_column(
        sa.Enum("M", "F", name="gender_enum"), nullable=False
    )
    ssn: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False, index=True)
    dob: so.Mapped[date] = so.mapped_column(sa.Date, nullable=True)
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), unique=True, nullable=False, index=True
    )
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    role_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("roles.id"), nullable=False, index=True
    )
    role: so.Mapped["Role"] = so.relationship("Role", back_populates="users")
    phone_numbers: so.Mapped[List["PhoneNumber"]] = so.relationship(
        "PhoneNumber", back_populates="user"
    )
    pic_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("uploaded_files.id"), nullable=True
    )
    _pic: so.Mapped["UploadedFile"] = so.relationship(
        "UploadedFile", back_populates="user", uselist=False
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
        default_file = UploadedFile.query.filter_by(filename="default.png").first()
        if not default_file:
            raise ValueError(
                "Default profile picture 'default.png' not found in database"
            )

        return default_file
