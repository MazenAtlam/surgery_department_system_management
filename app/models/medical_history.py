import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from patient import Patient


class MedicalHistory(BaseModel):
    __tablename__ = "medical_history"

    name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False, index=True)
    family_history: so.Mapped[bool] = so.mapped_column(sa.Boolean, nullable=True)
    patient_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("patients.id"), nullable=False, index=True
    )
    patient: so.Mapped["Patient"] = so.relationship("Patient", back_populates="medical_history")
