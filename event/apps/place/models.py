from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
    name = models.CharField(max_length='100')
    purpose = models.CharField(max_length='255')
#    coordinates = LocationField(blank=True, max_length=255)

    def upload_to(self, filename):
            return 'organizations/%s/%s' % (self.name, filename)

    banner = models.ImageField(upload_to=upload_to)

    def __unicode__(self):
        return self.name