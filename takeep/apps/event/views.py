from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from apps.accounts.views import my_event
from apps.event.actions import (send_joinrequest_mail, send_eventchange_mail,
    send_approval_mail, send_disapproval_mail, send_cancellation_mail)
from apps.event.forms import EventForm, EventReportForm
from apps.event.models import Event, Participant


def events(request):
    all_events = Event.objects.filter(
        status="O").select_related()
    paginator = Paginator(all_events, 8)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        upcoming_events = paginator.page(page)
    except (EmptyPage, InvalidPage):
        upcoming_events = paginator.page(paginator.num_pages)
    return render(request, 'event/events.html',
        {'upcoming_events': upcoming_events})

@login_required
def past_events(request):
    all_events = Event.objects.filter(
        status="C").select_related()
    paginator = Paginator(all_events, 8)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    try:
        past_events = paginator.page(page)
    except (EmptyPage, InvalidPage):
        past_events = paginator.page(paginator.num_pages)
    return render(request, 'event/past_events.html',
        {'past_events': past_events})


@login_required
def event(request, event_id):
    """
    Particular events page
    """
    event = get_object_or_404(Event, id=event_id)
    participations = Participant.objects.filter(event=event)
    return render(request, 'event/event.html',
        {'event': event,
        'participations': participations})


@login_required
def create_event(request):
    """
    To create an event
    """
    if request.POST:
        eventform = EventForm(request.POST, request.FILES)
        if eventform.is_valid():
            eventform.save(request)
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
            eventform = EventForm(request.POST, request.FILES, instance=event)
            if eventform.is_valid():
                eventform.save(request)
                send_eventchange_mail(event_id)
                messages.add_message(request, messages.SUCCESS,
                    'Your event changed as your requested.')
                return HttpResponseRedirect('/')
            else:
                return render(request, 'event/edit_event.html',
                    {'form': eventform})
        else:
            eventform = EventForm(instance=event)
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
        user = User.objects.get(id=user_id)
        Participant.objects.filter(event=event, guest=user).update(is_approved=True)
        send_approval_mail(event_id, user_id)
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
        user = User.objects.get(id=user_id)
        Participant.objects.filter(event=event, guest=user).update(is_approved=False)
        send_disapproval_mail(event_id, user_id)
        messages.add_message(request, messages.SUCCESS,
                    'The invitation disapproved as your requested.')
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
        return HttpResponseRedirect('/')
    return my_event(request, event_id)


@login_required
def cancel_event(request, event_id):
    """
    Cancel an event
    """
    event = get_object_or_404(Event, id=event_id)
    if request.user.id == event.host.id:
        """
        can cancel the event
        """
        event.status = "Q"
        event.save()
        send_cancellation_mail(event_id)
    else:
        messages.add_message(request, messages.ERROR,
            'You can not edit this event, because you are not the host of it.')
    return HttpResponseRedirect('/')


@login_required
def join(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participate_tuple = Participant.objects.get_or_create(guest=request.user, event=event)
    participate = participate_tuple[0]
    result = participate_tuple[1]
    if not result:
        if participate.is_approved:
            messages.add_message(request, messages.ERROR,
                'You are already attending to this event.')
        else:
            messages.add_message(request, messages.ERROR,
                'You already have a not approved request for this event.')
    else:
        if event.is_private:
            send_joinrequest_mail(request.user, event_id)
            messages.add_message(request, messages.ERROR,
                'You request is waiting approval by the host of the event.')
        else:
            participate.is_approved = True
            participate.save()
    participations = Participant.objects.filter(event=event)
    return render(request, 'event/event.html',
        {'event': event,
        'participations': participations})


@login_required
def report(request, event_id):
    """
    To report the event
    """
    event = get_object_or_404(Event, id=event_id)
    user = request.user
    if request.POST:
        reportform = EventReportForm(request.POST)
        if reportform.is_valid():
            reportform.save(user, event)
            messages.add_message(request, messages.WARNING,
                'Your event created as your requested.')
            return HttpResponseRedirect('/')
        else:
            return render(request, 'event/report.html',
                {'form': reportform})
    else:
        reportform = EventReportForm()
        return render(request, 'event/report.html',
            {'form': reportform})
