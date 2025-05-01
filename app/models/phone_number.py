import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class PhoneNumber(BaseModel):
    __tablename__ = "phone_numbers"

    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False
    )
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="phone_numbers")
    number: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False, unique=True)
