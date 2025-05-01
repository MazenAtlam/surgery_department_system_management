from typing import List

import sqlalchemy.orm as so
from .base_model import BaseModel
import app.models as m


class Role(BaseModel):
    __tablename__ = "roles"
    name: so.Mapped[str] = so.mapped_column(unique=True)
    users: so.Mapped[List["m.User"]] = so.relationship("User", back_populates="role")
