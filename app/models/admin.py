from base_model import BaseModel
from user import User


class Admin(BaseModel, User):
    __abstract__ = False
    __tablename__ = "admins"
