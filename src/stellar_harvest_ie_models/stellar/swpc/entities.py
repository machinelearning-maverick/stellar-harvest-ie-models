from sqlalchemy import Column, Integer, String, DateTime, Float
from .db import Base


class KpIndexEntity(Base):
    __tablename__ = "kp_index"
    id = Column(Integer, primary_key=True, index=True)
    time_tag = Column(DateTime, index=True)
    kp_index = Column(Integer)
    estimated_kp = Column(Float)
    kp = Column(String)
