from sqlalchemy import String, Integer, Float, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from models.base import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    agency: Mapped[str] = mapped_column(String(50))
    agency_type: Mapped[str] = mapped_column(String(50))
    distribution_channel: Mapped[str] = mapped_column(String(50))
    product_name: Mapped[str] = mapped_column(String(100))
    destination: Mapped[str] = mapped_column(String(100))

    duration: Mapped[int] = mapped_column(Integer)
    net_sales: Mapped[float] = mapped_column(Float)
    commission: Mapped[float] = mapped_column(Float)
    age: Mapped[int] = mapped_column(Integer)

    is_refund: Mapped[str] = mapped_column(String(10))
    suspected_fraud: Mapped[str] = mapped_column(String(10))
    commission_rate: Mapped[float] = mapped_column(Float)

    # Prediction result
    prediction_class: Mapped[int] = mapped_column(Integer)
    prediction_probability: Mapped[float] = mapped_column(Float)

    # Model tracking
    model_version: Mapped[str] = mapped_column(String(50))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )