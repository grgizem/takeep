from django.db import models
from django.contrib.auth.models import User
from apps.place.models import Place


class Event(models.Model):
    host = models.ForeignKey(User, related_name='is_host')
    title = models.CharField(max_length='100')
    description = models.CharField(max_length='255')
    location = models.ForeignKey(Place, related_name='had_events')
    is_private = models.BooleanField(default=False)
    tags = models.CharField(max_length=255,
                            blank=True,
                            null=True
                            )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def upload_to(self, filename):
            return 'events/%s/%s' % (self.title, filename)

    banner = models.ImageField(upload_to=upload_to)

    def __unicode__(self):
        return self.title


class Participant(models.Model):
    event = models.ForeignKey(Event, related_name='participants')
    guest = models.ForeignKey(User, related_name='attended_to')
    is_approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('event', 'guest')
