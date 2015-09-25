# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from faker import Faker

from fossevents.events.models import Event

NUM_EVENTS = getattr(settings, "NUM_EVENTS", 10)


class Command(BaseCommand):
    fake = Faker()

    @transaction.atomic
    def handle(self, *args, **options):
        self.fake.seed(4321)
        self.events = []

        print('  Updating domain to localhost:8000')  # Update site url
        site = Site.objects.get_current()
        site.domain, site.name = 'localhost:8000', 'Local'
        site.save()

        print('  Creating Superuser')  # create superuser
        self.create_user(is_superuser=True, username='admin', email='admin@fossevents.in',
                         is_active=True, is_staff=True)

        print(' Creating Events')
        for num in range(0, NUM_EVENTS):
            self.create_event()

    def create_user(self, counter=None, **kwargs):
        params = {
            "first_name": kwargs.get('first_name', self.fake.first_name()),
            "last_name": kwargs.get('last_name', self.fake.last_name()),
            "username": kwargs.get('username', self.fake.user_name()),
            "email": kwargs.get('email', self.fake.email()),
            "is_active": kwargs.get('is_active', self.fake.boolean()),
            "is_superuser": kwargs.get('is_superuser', False),
            "is_staff": kwargs.get('is_staff', kwargs.get('is_superuser', self.fake.boolean())),
        }
        user = get_user_model().objects.create(**params)
        password = '123123'

        user.set_password(password)
        user.save()

        print("User created with username: {username} and password: {password}".format(
              username=params['username'], password=password))

        return user

    def create_event(self, counter=None, **kwargs):
        params = {
            'name': kwargs.get('name', self.fake.sentence()),
            'description': requests.get('http://jaspervdj.be/lorem-markdownum/markdown.txt').content,
            'start_date': timezone.now(),
            'end_date': timezone.now(),
            'homepage': self.fake.url(),
            'is_published': True,
            'auth_token': self.fake.md5(),
            'owner_email': self.fake.email(),
        }
        event = Event.objects.create(**params)
        return event
