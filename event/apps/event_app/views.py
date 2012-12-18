from django.shortcuts import render


def events(request):
    return render(request, 'events.html')


def event(request):
    return render(request, 'event.html')


def create_event(request):
    return render(request, 'create_event.html')


def edit_event(request):
    return render(request, 'edit_event.html')
