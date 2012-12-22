from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from event_app.forms import EventForm
from event_app.models import Event


@login_required
def profile(request):
    """
    Profle page of logged-in user
    """
    return render(request, 'profile.html')


def events(request):
    """
    All events page
    """
    return render(request, 'events.html')


def event(request):
    """
    Particular events page
    """
    return render(request, 'event.html')


@login_required
def create_event(request):
    """
    To create an event
    """
    return render(request, 'create_event.html')


@login_required
def edit_event(request, event_id):
    """
    To edit an existence event
    """
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    if user.id == event.host.id:
        if request.POST:
            eventform = EventForm(request.POST)
            if eventform.is_valid():
                eventform.save(user)
                messages.add_message(request, messages.WARNING,
                    'Your event changed as your requested.')
                return HttpResponseRedirect('/')
            else:
                return render(request, 'edit_event.html', {'form': eventform})
        else:
            eventform = EventForm(event)
            return render(request, 'edit_event.html',
                {'event_id': event_id, 'form': eventform})
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')
