# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from fossevents.base.mail import send_email

from . import models

User = get_user_model()


def get_public_event_listings(search_term=None):
    qs = models.Event.objects.filter(is_published=True)
    qs = qs.order_by('-start_date')
    if search_term:
        qs = qs.filter(name__icontains=search_term)
    return qs


def get_chronologically_sorted_events():
    time_now = timezone.now()
    upcoming_events = models.Event.objects.filter(is_published=True, end_date__gte=time_now)
    past_events = models.Event.objects.filter(is_published=True, end_date__lte=time_now)
    return upcoming_events, past_events


def send_event_create_mail(event, moderators_email):

    current_site = Site.objects.get_current()
    extra_context = {'event': event, 'site_url': '{}://{}'.format(settings.SITE_SCHEME, current_site.domain)}

    # Send mail to moderators
    send_email('FOSSEvents | ' + event.name[:15] + ' published!',
               'email/event_create_moderators_email.txt', moderators_email,
               extra_context, 'email/event_create_moderators_email.html')

    # Send mail to creator
    send_email('FOSSEvents | ' + event.name[:15] + ' published!',
               'email/event_create_creator_email.txt', [event.owner_email],
               extra_context, 'email/event_create_creator_email.html')


def send_event_update_mail(event, moderators_email):

    current_site = Site.objects.get_current()
    extra_context = {'event': event, 'site_url': '{}://{}'.format(settings.SITE_SCHEME, current_site.domain)}

    # Send mail to moderators
    send_email('FOSSEvents | ' + event.name[:15] + ' updated!',
               'email/event_update_moderators_email.txt', moderators_email,
               extra_context, 'email/event_update_moderators_email.html')

    # Send mail to creator
    send_email('FOSSEvents | ' + event.name[:15] + ' updated!',
               'email/event_update_creator_email.txt', [event.owner_email],
               extra_context, 'email/event_update_creator_email.html')


def send_confirmation_mail(event, is_update=False):
    """
    Send mails about new event creation.

    :param event object
    :param is_update boolean
    """

    # get all end users both candidates and employers
    moderators_email = User.objects.filter(is_staff=True).values_list('email', flat=True)

    if is_update:
        return send_event_update_mail(event, moderators_email)

    return send_event_create_mail(event, moderators_email)
