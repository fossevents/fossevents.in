# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.utils import timezone

from fossevents.events.models import Event


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(' Creating events')
        self.events = self.create_events()
        print(' events created')

    def create_events(self):
        for count in range(0, 20):
            Event.objects.create(**{
                'name': "name %d" % count,
                'description': "%d description" % count,
                'start_date': timezone.now(),
                'end_date': timezone.now(),
                'homepage': "www.google.com",
                'is_published': True,
                'auth_token': "12345",
                'owner_email': "example@gmail.com",
            })
