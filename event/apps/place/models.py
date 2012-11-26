from django.db import models
from django.contrib.auth.models import User
# place model , just for test purposes , more to be added later


class Place(models.Model):
    owner = models.ForeignKey(User, related_name='organization')
    name = models.CharField(max_length='100')
    purpose = models.CharField(max_length='255')
    visitor = models.ManyToManyField(User, related_name=u'list_of_visitors')
#    location = LocationField(blank=True, max_length=255)

    def upload_to(self, filename):
            return 'organizations/%s/%s' % (self.name, filename)

    banner = models.ImageField(upload_to=upload_to)

    class Meta:
        verbose_name = ('Place')
        verbose_name_plural = ('Places')

    def __unicode__(self):
        return self.name
