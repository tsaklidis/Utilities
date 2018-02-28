from django.utils import timezone
# returns the date after given days


def days_hence(d=1):
    return timezone.now() + timezone.timedelta(days=d)
