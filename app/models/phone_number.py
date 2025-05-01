import sqlalchemy as sa
import sqlalchemy.orm as so
from .base_model import BaseModel
import app.models as m


class PhoneNumber(BaseModel):
    __tablename__ = "phone_numbers"

    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False
    )
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="phone_numbers")
    number: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False, unique=True)
