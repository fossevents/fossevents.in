# -*- coding: utf-8 -*
from django.shortcuts import render

from fossevents.events import services as event_services


def homepage(request):
    search_term = request.GET.get('q', None)
    ctx = {
        'events': event_services.get_public_event_listings(search_term=search_term)
    }
    return render(request, 'home.html', ctx)
