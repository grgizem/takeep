from django.db import models
from django.contrib.auth.models import User
from apps.place.models import Place


class Event(models.Model):
    host = models.ForeignKey(User, related_name='is_host')
    title = models.CharField(max_length='100')
    description = models.CharField(max_length='255')
    participant = models.ManyToManyField(User, related_name=u'attended_events')
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
