"""Date and time utility functions for daily use."""

import calendar
from datetime import date, timedelta


def days_between(start: date, end: date) -> int:
    """Return the number of days between *start* and *end* (inclusive of sign).

    Example:
        >>> from datetime import date
        >>> days_between(date(2024, 1, 1), date(2024, 1, 10))
        9
    """
    return (end - start).days


def start_of_week(d: date) -> date:
    """Return the Monday of the week that contains *d*.

    Example:
        >>> from datetime import date
        >>> start_of_week(date(2024, 4, 3))  # Wednesday
        datetime.date(2024, 4, 1)
    """
    return d - timedelta(days=d.weekday())


def end_of_week(d: date) -> date:
    """Return the Sunday of the week that contains *d*.

    Example:
        >>> from datetime import date
        >>> end_of_week(date(2024, 4, 3))  # Wednesday
        datetime.date(2024, 4, 7)
    """
    return d + timedelta(days=6 - d.weekday())


def is_weekend(d: date) -> bool:
    """Return ``True`` if *d* falls on a Saturday or Sunday.

    Example:
        >>> from datetime import date
        >>> is_weekend(date(2024, 4, 6))  # Saturday
        True
    """
    return d.weekday() >= 5


def friendly_date(d: date) -> str:
    """Return a human-friendly representation of *d*.

    Examples::

        "Today", "Yesterday", "Tomorrow", or "Mon 01 Apr 2024".

    Example:
        >>> from datetime import date
        >>> friendly_date(date.today())
        'Today'
    """
    today = date.today()
    delta = (d - today).days
    if delta == 0:
        return "Today"
    if delta == -1:
        return "Yesterday"
    if delta == 1:
        return "Tomorrow"
    return f"{calendar.day_abbr[d.weekday()]} {d.day:02d} {calendar.month_abbr[d.month]} {d.year}"
