from datetime import datetime, timezone, timedelta

def date_now():
  return datetime.now(timezone(timedelta(hours=-3)))