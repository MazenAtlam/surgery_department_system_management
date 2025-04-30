from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


def gen_datetime():
    """
    Generate the current datetime in UTC timezone
    Returns:
        datetime: current datetime in UTC timezone
    """
    return datetime.utcnow()


class BaseModel(db.Model):
    """
        Base model class
        Args:
            db (): Database object
        """

    __abstract__ = True
    id: so.Mapped[str] = so.mapped_column(
        sa.String(128), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    created_at: so.Mapped[sa.DateTime] = so.mapped_column(
        sa.DateTime, default=gen_datetime
    )
    updated_at: so.Mapped[sa.DateTime] = so.mapped_column(
        sa.DateTime, default=gen_datetime, onupdate=gen_datetime
    )
    deleted_at: so.Mapped[Optional[sa.DateTime]] = so.mapped_column(
        sa.DateTime, nullable=True
    )