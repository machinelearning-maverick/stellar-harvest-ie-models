from sqlalchemy import (
    BigInteger,
    Column,
    Integer,
    SmallInteger,
    String,
    DateTime,
    Float,
    UniqueConstraint,
    func,
)
from stellar_harvest_ie_models.base import Base


class KpIndexEntity(Base):
    __tablename__ = "kp_index"
    id = Column(Integer, primary_key=True, index=True)
    time_tag = Column(DateTime, index=True)
    kp_index = Column(Integer)
    estimated_kp = Column(Float)
    kp = Column(String)

    def __repr__(self):
        return (
            f"KpIndexEntity(id={self.id}, "
            f"time_tag={self.time_tag}, "
            f"kp_index={self.kp_index}, "
            f"estimated_kp={self.estimated_kp}, "
            f"kp='{self.kp}')"
        )


class KpForecastEntity(Base):
    __tablename__ = "kp_forecast"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    forecast_time = Column(DateTime(timezone=True), nullable=False)
    issued_at = Column(DateTime(timezone=True), nullable=False)
    horizon = Column(SmallInteger, nullable=False)
    predicted_kp = Column(Float, nullable=False)
    predicted_g = Column(SmallInteger, nullable=False)
    model_name = Column(String, nullable=False)
    model_version = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        UniqueConstraint(
            "forecast_time", "issued_at", "model_version", name="kp_forecast_unique_run"
        ),
    )

    def __repr__(self):
        return (
            f"KpForecastEntity(id={self.id}, "
            f"forecast_time={self.forecast_time}, "
            f"issued_at={self.issued_at}, "
            f"horizon={self.horizon}, "
            f"predicted_kp={self.predicted_kp}, "
            f"predicted_g={self.predicted_g}, "
            f"model_name='{self.model_name}', "
            f"model_version='{self.model_version}', "
            f"created_at={self.created_at})"
        )
