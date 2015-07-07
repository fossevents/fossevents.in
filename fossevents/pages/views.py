# -*- coding: utf-8 -*
from django.shortcuts import render
from fossevents.events import services as event_services


def homepage(request):
    ctx = {
        'events': event_services.get_public_event_listings()
    }
    return render(request, 'pages/home.html', ctx)
