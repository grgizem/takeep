from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(null=True, max_length='100')
    last_name = models.CharField(null=True, max_length='100')
    e_mail = models.EmailField(null=True, verbose_name=u'email address', max_length='255')
    facebook = models.CharField(null=True, max_length='255')
