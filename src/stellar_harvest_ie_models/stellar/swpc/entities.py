from sqlalchemy import Column, Integer, String, DateTime, Float
from stellar_harvest_ie_models.base import Base


class KpIndexEntity(Base):
    __tablename__ = "kp_index"
    id = Column(Integer, primary_key=True, index=True)
    time_tag = Column(DateTime, index=True)
    kp_index = Column(Integer)
    estimated_kp = Column(Float)
    kp = Column(String)

    def __str__(self):
        return (
            f"KpIndexEntity(id={self.id}, "
            f"time_tag={self.time_tag}, "
            f"kp_index={self.kp_index}, "
            f"estimated_kp={self.estimated_kp}, "
            f"kp='{self.kp}'"
        )
