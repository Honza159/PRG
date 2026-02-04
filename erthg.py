import calendar
from datetime import datetime, timedelta, timezone, date
from zoneinfo import ZoneInfo
import pandas as pd

print(calendar.month(2026, 3))
print(calendar.weekday(2026, 2, 4))
print(calendar.month(2026, 2))

start = datetime.now(ZoneInfo('Europe/Prague'))
print((start + timedelta(days=30)).replace(hour=9, minute=0, second=0, microsecond=0))


now_ny = datetime.now(ZoneInfo('America/New_York'))
print(now_ny)


today = date.today()
y, m = (today.year + (today.month ==12), 1) if today.month == 12 else (today.year, today.month + 1)
d = date(y, m, 1)
while d.weekday() >= 5:
    d += timedelta(days=1)
print(d)


def fmt_dur(seconds: int) -> str:
    td = timedelta(seconds=seconds)
    s = int(td.total_seconds())
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)
    return print(f'{h:02d}:{m:02d}:{s:02d}')
fmt_dur(3600*6 + 420)

s = pd.to_datetime(
    ['2026-01-23 14:00', '2026-03-28 02:30'],
    utc=True
)
print(s.tz_convert('Europe/Prague'))


start_utc = datetime(2026, 1, 23, 7, 30, tzinfo=timezone.utc)
end_utc = datetime(2026, 1, 23, 8, 45, tzinfo=timezone.utc)
tz = ZoneInfo("Europe/Prague")
start = start_utc.astimezone(tz).strftime("%d.%m.%Y %H:%M")
end = end_utc.astimezone(tz).strftime("%H:%M")
print(f"Schůzka s Frantou Novákem: {start}-{end}")