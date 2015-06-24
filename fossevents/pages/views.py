from django.shortcuts
from fossevents.events
import render
import services as event_services

def homepage(request):
    ctx = {
        'events': event_services.get_public_event_listings()
    }
return render(request, 'pages/home.html', ctx)
