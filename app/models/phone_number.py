import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class PhoneNumber(BaseModel):
    __tablename__ = "phone_numbers"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False
    )
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="phone_numbers")
    number: so.Mapped[str] = so.mapped_column(
        sa.String(11), nullable=False, unique=True
    )
