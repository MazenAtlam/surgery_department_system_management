import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db


class Role(BaseModel):
    __tablename__ = "roles"
    name: so.Mapped[str] = so.mapped_column(unique=True)
