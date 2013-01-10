from haystack import indexes
from haystack import site
from apps.place.models import Place


class PlaceIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    coordinates = indexes.CharField(model_attr='coordinates')
    address = indexes.CharField(model_attr='address')

    def get_model(self):
        return Place

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(is_approved=True)


site.register(Place, PlaceIndex)
