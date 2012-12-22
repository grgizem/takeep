from django.db import models


class Place(models.Model):
    name = models.CharField("Place Name", max_length='100')
    description = models.CharField("Description", max_length='255')
    coordinates = models.CharField("Geolocation", blank=True, max_length=100)
    address = models.CharField("Address",
                               max_length=255,
                               blank=True,
                               null=True
                               )
    phone_number = models.CharField("Phone Number",
                                    max_length=11,
                                    blank=True,
                                    null=True
                                    )

    email = models.EmailField("E-Mail", blank=True, null=True,)
    webpage = models.URLField("Webpage", blank=True, null=True,)

    def upload_to(self, filename):
            return 'organizations/%s/%s' % (self.name, filename)

    banner = models.ImageField(upload_to=upload_to)

    def __unicode__(self):
        return self.name
