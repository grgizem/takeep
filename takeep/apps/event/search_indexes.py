import datetime
from haystack import indexes
from haystack import site
from apps.event.models import Event


class EventIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    host = indexes.CharField(model_attr='host')
    location = indexes.CharField(model_attr='location')
    start_time = indexes.DateTimeField(model_attr='start_time')

    def get_model(self):
        return Event

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(start_time__lte=datetime.datetime.now())

site.register(Event, EventIndex)
