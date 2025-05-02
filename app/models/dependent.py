import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class Dependent(BaseModel):
    __tablename__ = "dependents"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    dependent_name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    dependent_phone_number: so.Mapped[str] = so.mapped_column(
        sa.String(50), nullable=False
    )
    patient_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("patients.id"), nullable=False
    )
    patient: so.Mapped["m.Patient"] = so.relationship(
        "Patient", back_populates="dependents"
    )
