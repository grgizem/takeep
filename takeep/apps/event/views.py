from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.accounts.views import my_event
from apps.event.forms import EventForm
from apps.event.models import Event, Participant


def events(request):
    """
    All events page
    """
    return render(request, 'events.html')


@login_required
def event(request, event_id):
    """
    Particular events page
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event/event.html', {'event': event})


@login_required
def create_event(request):
    """
    To create an event
    """
    user = request.user
    if request.POST:
        eventform = EventForm(request.POST)
        if eventform.is_valid():
            eventform.save(user)
            messages.add_message(request, messages.WARNING,
                'Your event created as your requested.')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'event/create_event.html',
                {'form': eventform})
    else:
        eventform = EventForm()
        return render(request, 'event/create_event.html',
            {'form': eventform})


@login_required
def edit_event(request, event_id):
    """
    To edit an existence event
    """
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    if user.id == event.host.id:
        """
        The user can edit the event if he/she is the host of it
        """
        if request.POST:
            eventform = EventForm(request.POST)
            if eventform.is_valid():
                eventform.save(user)
                messages.add_message(request, messages.SUCCESS,
                    'Your event changed as your requested.')
                return HttpResponseRedirect('/')
            else:
                return render(request, 'event/edit_event.html',
                    {'form': eventform})
        else:
            eventform = EventForm(event)
            return render(request, 'event/edit_event.html',
                {'event_id': event_id, 'form': eventform})
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')


@login_required
def approve(request, event_id, user_id):
    """
    Approvement action
    """
    event = get_object_or_404(Event, id=event_id)
    if request.user.id == event.host.id:
        """
        Then the requested user can approve the partcipation
        """
        participant = Participant(event__id=event_id, host__id=user_id)
        participant.is_approved = True
        participant.save()
        messages.add_message(request, messages.SUCCESS,
                    'The invtation approved as your requested.')
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')
    return my_event(request, event_id)


@login_required
def disapprove(request, event_id, user_id):
    """
    Approvement action
    """
    event = get_object_or_404(Event, id=event_id)
    if request.user.id == event.host.id:
        """
        Then the requested user can approve the partcipation
        """
        participant = Participant(event__id=event_id, host__id=user_id)
        participant.is_approved = False
        participant.save()
        messages.add_message(request, messages.SUCCESS,
                    'The invitation disapproved as your requested.')
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')
    return my_event(request, event_id)


@login_required
def cancel_event(request):
    """
    All events page
    """
    return render(request, 'events.html')
