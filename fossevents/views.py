# -*- coding: utf-8 -*
from django.shortcuts import render

from fossevents.events import services as event_services


def homepage(request):
    search_term = request.GET.get('q', None)
    upcoming_events = past_events = list()
    if not search_term:
        upcoming_events, past_events = event_services.get_chronologically_sorted_events()
    ctx = {
        'events': event_services.get_public_event_listings(search_term=search_term) if search_term else [],
        'upcoming_events': upcoming_events,
        'past_events': past_events
    }
    return render(request, 'home.html', ctx)
