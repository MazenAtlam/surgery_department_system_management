from typing import List

import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    name: so.Mapped[str] = so.mapped_column(unique=True, nullable=False)
    users: so.Mapped[List["m.User"]] = so.relationship("User", back_populates="role")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
