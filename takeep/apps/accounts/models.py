from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):

    FEMALE = 'F'
    MALE = 'M'

    GENDER_CHOICES = (
        (FEMALE, 'FEMALE'),
        (MALE, 'MALE'),
    )

    ISTANBUL = "34"
    ANKARA = "06"
    IZMIR = "35"
    OTHER = "00"

    LOCATION_CHOICES = (
        (ISTANBUL, "Istanbul"),
        (ANKARA, "Ankara"),
        (IZMIR, "Izmir"),
        (OTHER, "Other"),
    )

    def upload_to(self, filename):
            return 'users/%s/%s' % (self.user.username, filename)

    user = models.OneToOneField(User)

    gender = models.CharField("Gender",
                                max_length=1,
                                choices=GENDER_CHOICES,
                                blank=True,
                                null=True,
                                )
    birthdate = models.DateField("Birthdate",
                                 blank=True,
                                 null=True,
                                 )
    address = models.TextField("Address",
                               blank=True,
                               null=True,
                               )
    photo = models.ImageField("Profile Photo",
                              upload_to=upload_to,
                              null=True,
                              blank=True
                              )
    location = models.CharField("City",
                                max_length=2,
                                choices=LOCATION_CHOICES,
                                blank=True,
                                null=True,
                                )
    bio = models.TextField("Biography",
                           max_length=255,
                           blank=True,
                           null=True,
                           )


@receiver(post_save, sender=User)
def post_user_creation_handler(sender, instance, *args, **kwargs):
    user = instance
    UserProfile.objects.get_or_create(user=user)

# To be sure every User has an UserProfile.
post_save.connect(post_user_creation_handler, sender=User)
