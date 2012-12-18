from django.shortcuts import render


def profile(request):
    return render(request, 'profile.html')


def edit_profile(request):
    return render(request, 'edit_profile.html')


def my_events(request):
    return render(request, 'my_events.html')


def my_event(request):
    return render(request, 'my_event.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def logout(request):
    return render(request, 'logout.html')
