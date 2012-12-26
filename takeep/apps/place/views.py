from django.shortcuts import render, get_object_or_404

from apps.place.models import Place


def places(request):
    places = Place.objects.all()
    return render(request, 'place/places.html', {'places': places})


def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    events = place.had_events.all()
    return render(request, 'place/place.html',
        {'place': place, 'events': events})


def create_place(request):
    return render(request, 'place/create_place.html')


def flag(request, place_id):
    return render(request, 'place/flag.html')
