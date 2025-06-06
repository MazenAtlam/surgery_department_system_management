import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Admin(BaseModel):
    __abstract__ = False
    __tablename__ = "admins"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    is_superadmin: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)

    user_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id"), nullable=False, unique=True
    )
    user: so.Mapped["m.User"] = so.relationship("User", back_populates="admin")
