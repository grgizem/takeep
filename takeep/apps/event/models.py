import datetime

from django.db import models
from django.contrib.auth.models import User
from apps.place.models import Place


class Event(models.Model):
    host = models.ForeignKey(User, related_name='is_host',
                             blank=True,
                             null=True)
    """
    The host of the event;
    - if event is a hosted by someone, this will be that user
    - in other events this field will be blank
    """
    OPEN = 'O'
    CLOSED = 'C'
    CANCELLED = 'Q'

    STATE_CHOICES = (
        # the event will take place.
        (OPEN, 'OPEN'),
        # the event is expired.
        (CLOSED, 'CLOSED'),
        # the event is cancelled.
        (CANCELLED, 'CANCELLED'),
    )
    """
    The Event has status options as it below.
    """
    title = models.CharField(max_length='100')
    """
    The title of the event
    """
    description = models.CharField(max_length='255')
    """
    The description of the event
    """
    location = models.ForeignKey(Place, related_name='had_events')
    """
    The location of the event, will be the place object from the database
    """
    is_private = models.BooleanField(default=False)
    """
    This field;
    - True, if this events participants will be approved by the host
    - False, if it is an open event
    """
    tags = models.CharField(max_length=255,
                            blank=True,
                            null=True
                            )
    """
    The descriptive tags of the event
    """
    start_time = models.DateTimeField()
    """
    The start time of the event as date and time
    """
    end_time = models.DateTimeField()
    """
    The end time of the event as date and time
    """
    status = models.CharField(max_length=1,
                          choices=STATE_CHOICES,
                          default=OPEN)
    """
    The status of an event, choices above.
    """

    def upload_to(self, filename):
            return 'events/%s/%s' % (self.title, filename)

    banner = models.ImageField(upload_to=upload_to)
    """
    The banner photo of the event
    """
    def get_active_participants(self):
        return self.participants.filter(is_approved=True)

    active_participants = property(get_active_participants)
    """
    Active participants of certain event.
    """

    def __unicode__(self):
        return self.title

    """
    Update status of an event.
    """
    def update_status(self):
        if self.status == self.CANCELLED:
            pass
        elif datetime.datetime.now(self.time.tzinfo) > self.end_statime:
            self.status = self.CLOSED
        self.save()
        return self

    """
    Cancel an event.
    """
    def cancel(self):
        self.status = self.CANCELLED
        self.save()


class Participant(models.Model):
    """
    Participant table required for the private events
    """
    event = models.ForeignKey(Event, related_name='participants')
    """
    The event of the participation
    """
    guest = models.ForeignKey(User, related_name='attended_to')
    """
    The user of the participation
    """
    is_approved = models.BooleanField(default=False)
    """
    if it is a private event, that stores the approvement status
    """

    class Meta:
        unique_together = ('event', 'guest')
        """
        Since the user will be attend a particular event for once
        """
