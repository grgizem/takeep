from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.event.models import Event
from apps.place.forms import PlaceForm, FlagPlaceForm
from apps.place.models import Place


@login_required
def places(request):
    """
    Shows all places with pagination and favorite places at the nav bar
    """
    all_places = Place.objects.filter(is_approved=True)
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
    """
    Show details of a specific place and events on that location
    """
    place = get_object_or_404(Place, id=place_id)
    if place.is_approved:
        """
        If the place is approved, shows details,
        - otherwise shows an error
        """
        events = place.had_events.all()
        return render(request, 'place/place.html',
            {'place': place, 'events': events})
    else:
        messages.add_message(request, messages.WARNING,
                'This place is waiting for the approvement.')
        return HttpResponseRedirect('/')


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
    """
    Flag the place to add extra information or correct misvalues
    """
    place = get_object_or_404(Place, id=place_id)
    if request.POST:
        flagform = FlagPlaceForm(request.POST, request.FILES)
        if flagform.is_valid():
            flagform.save(request, place)
            messages.add_message(request, messages.WARNING,
                'Place flag sent as your requested, waiting for approvement.')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'place/flag.html',
                {'place': place, 'form': flagform})
    else:
        flagform = PlaceForm(instance=place)
        return render(request, 'place/flag.html',
            {'place': place, 'form': flagform})
