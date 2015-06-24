from django.core.management.base import BaseCommand, CommandError
from fossevents.events.modelsimport Event
from django.utils import timezone

class Command(BaseCommand):


    def handle(self, * args, * * options):
        print(' Creating events')
        self.events = self.create_events()
        print(' events created')


    def create_events(self):
        for count in range(0, 20):
    	   Event.objects.create( * * {
 	        'name': "name %d" % count,
            'description': "%d description" % count,
            'start_date': timezone.now(),
            'end_date': timezone.now(),
            'homepage': "www.google.com",
            'is_published': True,
            'auth_token': "12345",
            'owner_email': "kushagra43@gmail.com",
            })
        return
