# -*- coding: utf-8 -*
from django.shortcuts import render
from fossevents.events import services as event_services
from fossevents.events.models import Event

def homepage(request):
    ctx = {
        'events': event_services.get_public_event_listings()
    }
    return render(request, 'pages/home.html', ctx)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            events = Event.objects.filter(name__icontains=q)
            return render(request, 'pages/home.html', {'events': events})
    ctx = {
        'events': event_services.get_public_event_listings()
    }
    return render(request, 'pages/home.html', ctx)
