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

    def __str__(self):
        return (
            f"KpIndexRecord(time_tag={self.time_tag}, "
            f"kp_index={self.kp_index}, "
            f"estimated_kp={self.estimated_kp}, "
            f"kp='{self.kp}', "
            f"mid_latitude_kp_index={self.mid_latitude_kp_index}, "
            f"dst={self.dst}, "
            f"source='{self.source}')"
        )
