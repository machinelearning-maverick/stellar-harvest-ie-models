from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class KpIndexRecord(BaseModel):
    """
    Represents a single reading of the Planetary K-Index from NOAA SWCP.
    Example: {"time_tag":"2025-05-11T08:55:00","kp_index":3,"estimated_kp":2.67,"kp":"3M"}
    """

    time_tag: datetime
    kp_index: int
    estimated_kp: float
    kp: str

    mid_latitude_kp_index: Optional[int] = None
    dst: Optional[float] = None
    source: Optional[str] = None
