import datetime

from core import settings


def get_current_time_with_tz() -> datetime.datetime:
    return datetime.datetime.now(tz=settings.DEFAULT_TIMEZONE)  # type: ignore
