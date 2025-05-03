import sqlalchemy as sa
import sqlalchemy.orm as so

import app.models as m

from .base_model import BaseModel


class MedicalHistory(BaseModel):
    __tablename__ = "medical_history"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    disease_name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False, index=True)
    family_history: so.Mapped[bool] = so.mapped_column(sa.Boolean, nullable=True)
    patient_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("patients.id"), nullable=False, index=True
    )
    patient: so.Mapped["m.Patient"] = so.relationship(
        "Patient", back_populates="medical_history"
    )
