from datetime import datetime
import pytz

def convert_timezone(dt_str: str, target_tz: str):
    try:
        ist = pytz.timezone("Asia/Kolkata")
        dt = datetime.fromisoformat(dt_str)
        dt = ist.localize(dt) if dt.tzinfo is None else dt
        return dt.astimezone(pytz.timezone(target_tz))
    except Exception:
        return None
