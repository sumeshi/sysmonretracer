from datetime import datetime

def parse_str_to_datetime(strdatetime: str) -> datetime:
    return datetime.strptime(strdatetime, "%Y-%m-%d %H:%M:%S.%f")
