from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.event.models import Event
from apps.place.forms import PlaceForm
from apps.place.models import Place


@login_required
def places(request):
    all_places = Place.objects.all()
    paginator = Paginator(all_places, 5)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        places = paginator.page(page)
    except (EmptyPage, InvalidPage):
        places = paginator.page(paginator.num_pages)

    events = Event.objects.filter(participants__guest=request.user)
    favorite_places_multi = Place.objects.filter(had_events__in=events)
    favorite_places = set(favorite_places_multi).intersection(set(places))
    return render(request, 'place/places.html',
        {'places': places, 'favorite_places': favorite_places})


@login_required
def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    events = place.had_events.all()
    return render(request, 'place/place.html',
        {'place': place, 'events': events})


@login_required
def create_place(request):
    """
    To create a place
    """
    if request.POST:
        placeform = PlaceForm(request.POST, request.FILES)
        if placeform.is_valid():
            placeform.save()
            messages.add_message(request, messages.WARNING,
                'Place created as your requested, waiting for approvement.')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'place/create_place.html',
                {'form': placeform})
    else:
        placeform = PlaceForm()
        return render(request, 'place/create_place.html',
            {'form': placeform})


@login_required
def flag(request, place_id):
    return render(request, 'place/flag.html')
