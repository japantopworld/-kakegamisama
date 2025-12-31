from datetime import datetime
from zoneinfo import ZoneInfo

def make_gate():
    now = datetime.now(ZoneInfo("Asia/Tokyo"))
    return f"KAMISAMA_{now.month:02d}_{now.day:02d}_{now.hour:02d}"
