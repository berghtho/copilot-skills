"""Tests for date_utils module."""

from datetime import date, timedelta

import pytest
from skills.date_utils import (
    days_between,
    end_of_week,
    friendly_date,
    is_weekend,
    start_of_week,
)


class TestDaysBetween:
    def test_positive_difference(self):
        assert days_between(date(2024, 1, 1), date(2024, 1, 10)) == 9

    def test_same_day(self):
        assert days_between(date(2024, 1, 1), date(2024, 1, 1)) == 0

    def test_negative_difference(self):
        assert days_between(date(2024, 1, 10), date(2024, 1, 1)) == -9


class TestStartOfWeek:
    def test_monday(self):
        assert start_of_week(date(2024, 4, 1)) == date(2024, 4, 1)

    def test_wednesday(self):
        assert start_of_week(date(2024, 4, 3)) == date(2024, 4, 1)

    def test_sunday(self):
        assert start_of_week(date(2024, 4, 7)) == date(2024, 4, 1)


class TestEndOfWeek:
    def test_monday(self):
        assert end_of_week(date(2024, 4, 1)) == date(2024, 4, 7)

    def test_wednesday(self):
        assert end_of_week(date(2024, 4, 3)) == date(2024, 4, 7)

    def test_sunday(self):
        assert end_of_week(date(2024, 4, 7)) == date(2024, 4, 7)


class TestIsWeekend:
    def test_saturday(self):
        assert is_weekend(date(2024, 4, 6)) is True

    def test_sunday(self):
        assert is_weekend(date(2024, 4, 7)) is True

    def test_monday(self):
        assert is_weekend(date(2024, 4, 1)) is False

    def test_friday(self):
        assert is_weekend(date(2024, 4, 5)) is False


class TestFriendlyDate:
    def test_today(self):
        assert friendly_date(date.today()) == "Today"

    def test_yesterday(self):
        assert friendly_date(date.today() - timedelta(days=1)) == "Yesterday"

    def test_tomorrow(self):
        assert friendly_date(date.today() + timedelta(days=1)) == "Tomorrow"

    def test_past_date(self):
        result = friendly_date(date(2024, 4, 1))
        assert result == "Mon 01 Apr 2024"

    def test_future_date(self):
        result = friendly_date(date(2030, 12, 25))
        assert result == "Wed 25 Dec 2030"
