from datetime import datetime, timezone

def utc_now() -> str:
    """Return UTC timestamp string."""
    return datetime.now(timezone.utc).isoformat()