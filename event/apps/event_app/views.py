from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.messages.api import get_messages

import random

from event_app.models import Event, Participant 
from django.contrib.auth.models import User
from social_auth.utils import setting

#logout
@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")


# profile page:
@login_required
def profile(request):
    return render_to_response('profile.html', RequestContext(request))

def events(request):
	
    return render(request, 'events.html')


def event(request):
    return render(request, 'event.html')


def create_event(request):
    return render(request, 'create_event.html')


#edit event
@login_required
def edit_event(request,event_id):
    e = get_object_or_404(Event, id=event_id)
    if request.user.id == e.host.id:
        if request.POST:
            eventform = EventForm(request.POST)
            if eventform.is_valid():
		eventform.save_as(request,e)
		messages.add_message(request, messages.WARNING, 'Your post is waiting for approvement.')
                return HttpResponseRedirect('/')
        else:
            eventform = EventForm({'title' : e.title, 'content' : e.content})
            return render_to_response('edit_event.html', {'event_id' : event_id, 'form' : eventform}, RequestContext(request))
    else:
        messages.add_message(request, messages.ERROR, 'You can not edit this post, because you are not the host of it.')
        return HttpResponseRedirect('/')
    return render(request, 'edit_event.html')
