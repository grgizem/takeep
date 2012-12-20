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

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")


def home(request):
    """Home view"""    
    if request.user.is_authenticated():	
        return render_to_response('profile.html', RequestContext(request))
    else:
	    return render_to_response('index.html', RequestContext(request))


def events(request):
	
    return render(request, 'events.html')


def event(request):
    return render(request, 'event.html')


def create_event(request):
    return render(request, 'create_event.html')


def edit_event(request):
    return render(request, 'edit_event.html')
