import sqlalchemy as sa
import sqlalchemy.orm as so
from base_model import BaseModel
from patient import Patient


class Dependent(BaseModel):
    __tablename__ = "dependents"

    dependent_name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    dependent_phone_number: so.Mapped[str] = so.mapped_column(
        sa.String(50), nullable=False
    )
    patient_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("patients.id"), nullable=False
    )
    patient: so.Mapped["Patient"] = so.relationship(
        "Patient", back_populates="dependents"
    )
