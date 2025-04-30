import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db


class User(BaseModel):
    __tablename__ = "user"

    email: so.Mapped[str] = so.mapped_column(unique=True)
    password: so.Mapped[str] = so.mapped_column()
