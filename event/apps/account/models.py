from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(null=True, max_length='100')
    last_name = models.CharField(null=True, max_length='100')
