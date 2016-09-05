# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from fossevents.base.mail import send_email

from . import models

User = get_user_model()


def get_public_event_listings(search_term=None):
    qs = models.Event.objects.filter(is_published=True)
    qs = qs.order_by('-start_date')
    if search_term:
        qs = qs.filter(name__icontains=search_term)
    return qs


def send_confirmation_mail(event):
    """
    Send mails about new event creation.
    """

    # get all end users both candidates and employers
    moderators_email = User.objects.filter(is_staff=True).values_list('email', flat=True)

    extra_context = {'event': event, 'event_link': ''}

    # Send mail to moderators
    send_email('An event is up for review',
               'email/event_moderators_email.txt', moderators_email,
               extra_context, 'email/event_moderators_email.html')

    # Send mail to creator
    send_email('An event has been created',
               'email/event_creator_email.txt', [event.owner_email],
               extra_context, 'email/event_creator_email.html')
    return
