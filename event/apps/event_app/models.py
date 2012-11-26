from django.db import models
from django.contrib.auth.models import User
# event model , just for test purposes , more to be added later


class Event(models.Model):
    host = models.ForeignKey(User, related_name='event')
    title = models.CharField(max_length='100')
    description = models.CharField(max_length='255')
    participants = models.ManyToManyField(User, related_name=u'list_of_parts')
#    location = LocationField(blank=True, max_length=255)

    def upload_to(self, filename):
            return 'events/%s/%s' % (self.title, filename)

    banner = models.ImageField(upload_to=upload_to)

    class Meta:
        verbose_name = ('Event')
        verbose_name_plural = ('Events')

    def __unicode__(self):
        return self.title
