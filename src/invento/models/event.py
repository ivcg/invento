from django.db import models

from organizations.models import Organization


class Event(models.Model):
    """
    An event entry for an organization.
    """
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    tagline = models.CharField(max_length=200, null=True, blank=True)
    organization = models.ForiegnKey(Organization, db_index=True)

    class Meta:
        db_table = 'events'


class SubEvent(models.Model):
    """
    A sub event under an event.
    """
    name = models.CharField(max_length=100, db_index=True)
    location = models.CharField(max_length=200, db_index=True)
    start_date = models.DateField()
    start_tine = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    recurring = models.BooleanField(default=False)

    class Meta:
        db_table = 'sub_events'
