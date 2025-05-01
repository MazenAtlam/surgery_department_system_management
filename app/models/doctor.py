from base_model import BaseModel
from user import User


class Doctor(BaseModel, User):

    __tablename__ = 'doctors'

