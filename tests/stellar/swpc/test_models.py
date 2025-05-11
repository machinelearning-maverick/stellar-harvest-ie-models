import pytest
from stellar_harvest_ie_models.stellar.swpc.models import KpIndexRecord
from datetime import datetime

def test_model_success():
    data = {
        "time_tag": "2025-04-21T23:45:00Z",
        "kp_index": 3,
        "estimated_kp": 4,
        "kp": "0P",
        "mid_latitude_kp_index": 4,
        "dst": -25.6,
    }

    record = KpIndexRecord(**data)
    assert record.kp_index == 3
    assert record.estimated_kp == 4
    assert isinstance(record.time_tag, datetime)

@pytest.mark.parametrize("bad", [
    {"time_tag": "invalid", "kp_index": 3, "mid_latitude_kp_index": 4, "dst": -25.6, "source": "NOAA"},
    {"time_tag": "2025-04-21T23:45:00Z", "kp_index": "x", "mid_latitude_kp_index": 4, "dst": -25.6, "source": "NOAA"},
    {}
])
def test_model_failure(bad):
    with pytest.raises(Exception):
        KpIndexRecord(**bad)
