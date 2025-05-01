import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db


class Department(BaseModel):
    __tablename__ = "departments"
    department_name: so.Mapped[str] = so.mapped_column(unique=True)
    department_location: so.Mapped[str] = so.mapped_column(unique=True)
