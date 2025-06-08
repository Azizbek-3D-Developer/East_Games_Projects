from fastapi.templating import Jinja2Templates
from datetime import datetime

templates = Jinja2Templates(directory="Templates")

def datetimeformat(value):
    if not value:
        return "N/A"
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Try parsing as ISO format string
        return datetime.fromisoformat(str(value)).strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        try:
            # Try parsing as Unix timestamp (float or int)
            return datetime.fromtimestamp(float(value)).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return str(value)

templates.env.filters["datetimeformat"] = datetimeformat
