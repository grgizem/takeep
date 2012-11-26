from django.db import models
from django.contrib.auth.models import User
# event model , just for test purposes , more to be added later


class Event(models.Model):
    host = models.ForeignKey(User, related_name='event')
    title = models.CharField(max_length='100')
    description = models.CharField(max_length='255')
    banner = models.ImageField(upload_to='events/%d, self.title')
    participants = models.ManyToManyField(User, related_name='list_of_parts')

    class Meta:
        verbose_name = ('Event')
        verbose_name_plural = ('Events')

    def __unicode__(self):
        return self.title


class Organization(models):
    owner = models.Foreignkey(User, related_name='organization')
    name = models.CharField(max_length='100')
    purpose = models.CharField(max_length='255')
    banner = models.ImageField(upload_to='organizations/%d, self.name')
    visitor = models.ManyToManyField(User, related_name=u'list_of_visitors')

    class Meta:
        verbose_name = ('Organization')
        verbose_name_plural = ('Organizations')

    def __unicode__(self):
        return self.name
