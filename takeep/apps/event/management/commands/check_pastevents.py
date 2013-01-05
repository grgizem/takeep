from datetime import datetime

from django.core.management.base import BaseCommand

from apps.event.models import Event

class Command(BaseCommand):
    help = 'Marking the event as closed if the end time is passed'

    def handle(self, *args, **options):
        events = Event.objects.filter(status="O")
        if events:
            now = datetime.utcnow().replace(tzinfo=None)
            for event in events:
                if event.end_time<=now:
                    event.status = "C"
                    event.save()
                    self.stdout.write('\nSuccessfully closed event "%s"."%s" ended at %s' % (event.id, event.title, event.end_time))
        else:
            self.stdout.write('\nThere is not an open event, you should better add some.')
