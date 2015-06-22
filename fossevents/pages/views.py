# -*- coding: utf-8 -*-
from django.shortcuts import render
from fossevents.events import services as event_services
from datetime import datetime
from fossevents.events.models import Event

def homepage(request):
# dummy data
    Event.objects.create(name="google",description="test123",homepage="www.google.com",is_published=True,auth_token=12345,owner_email="kushagra43@gmail.com",start_date=datetime.today(),end_date=datetime.today())			
# dummy end

    ctx = {
        'events': event_services.get_public_event_listings()
    }
    return render(request, 'pages/home.html', ctx)
