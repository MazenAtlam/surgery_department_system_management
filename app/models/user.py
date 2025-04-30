import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'user'

    email: so.Mapped[str] = so.mapped_column(unique=True)
    password: so.Mapped[str] = so.mapped_column()
