import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel

from app import db


class Patient(BaseModel):
    __tablename__ = "patients"
