from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.event.models import Event, Participant


@login_required
def profile(request):
    participations = Participant.objects.filter(guest=request.user, event.status="O")
    return render(request, 'accounts/profile.html', {'participate': participations})


@login_required
def edit_profile(request):
    return render(request, 'accounts/edit_profile.html')


@login_required
def my_events(request):
    events = Event.objects.filter(host=request.user)
    return render(request, 'accounts/my_events.html', {'events': events})


@login_required
def my_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.host.id == request.user.id:
        return render(request, 'accounts/my_event.html', {'event': event})
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')
