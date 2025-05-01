import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from user import User


class PhoneNumber(BaseModel):
    __tablename__ = "phone_numbers"

    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False
    )
    user: so.Mapped["User"] = so.relationship("User", back_populates="phone_numbers")
