import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db

from user import User
from typing import List
class Role(BaseModel):
    __tablename__ = "roles"
    name: so.Mapped[str] = so.mapped_column(unique=True)
    users: so.Mapped[List["User"]] = so.relationship("User", back_populates="role")
