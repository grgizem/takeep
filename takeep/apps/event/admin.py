from django.contrib import admin
from apps.event.models import Event, Participant

admin.site.register(Event)
admin.site.register(Participant)
