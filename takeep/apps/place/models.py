from django.db import models


class Place(models.Model):
    name = models.CharField("Place Name", max_length='100')
    """
    The Name of the place.
    """
    description = models.CharField("Description", max_length='255')
    """
    The Description of the place.
    """
    coordinates = models.CharField("Geolocation", blank=True, max_length=100)
    """
    The Coordinates of the place which is a geographical representation as
    longtitude and latitude.
    """
    address = models.CharField("Address",
                               max_length=255,
                               blank=True,
                               null=True
                               )
    """
    The Adress of the place which is an open presciriptive adress.
    """
    phone_number = models.CharField("Phone Number",
                                    max_length=11,
                                    blank=True,
                                    null=True
                                    )
    """
    The Phone number of the place.
    """
    email = models.EmailField("E-Mail", blank=True, null=True,)
    """
    The Email of the place.
    """
    webpage = models.URLField("Webpage", blank=True, null=True,)
    """
    The Webpage of the place.
    """

    def upload_to(self, filename):
            return 'organizations/%s/%s' % (self.name, filename)

    banner = models.ImageField(upload_to=upload_to)
    """
    The banner photo of the place.
    """

    def __unicode__(self):
        return self.name
