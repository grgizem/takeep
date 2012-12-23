from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.event.models import Event, Participant


@login_required
def profile(request):
    """
    Users own profile page
    """
    participations = Participant.objects.filter(
        guest=request.user, event__status="O")
    """
    will include the events that user will attend
    """
    suggestions = Participant.objects.exclude(
        guest=request.user).filter(event__status="O")
    """
    will include the suggested events
    """
    return render(request, 'accounts/profile.html',
        {'participations': participations,
        'suggestions': suggestions})


@login_required
def edit_profile(request):
    """
    profile editing page for user
    """
    return render(request, 'accounts/edit_profile.html')


@login_required
def my_events(request):
    events = Event.objects.filter(host=request.user)
    """
    will show the events of requested user
    """
    return render(request, 'accounts/my_events.html', {'events': events})


@login_required
def my_event(request, event_id):
    """
    users event, will show the details of the event
    and options for approve and disapprove the participations,
    edit event, close event
    """
    event = get_object_or_404(Event, id=event_id)
    if event.host.id == request.user.id:
        return render(request, 'accounts/my_event.html', {'event': event})
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')
