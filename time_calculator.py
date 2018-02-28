import datetime
from django.utils import timezone


# returns the date after given days
def days_hence(d=1):
    return timezone.now() + timezone.timedelta(days=d)


# Ensure age of at least 18 years old.
def over_18(birth_date=None):
    today = timezone.now().date()
    youth_threshold_day = (datetime.date(today.year - 18, today.month,
                                         today.day) +
                           datetime.timedelta(hours=24))
    if birth_date > youth_threshold_day:
        return False
    return True
