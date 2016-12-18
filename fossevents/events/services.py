# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.db.models import Q

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


def get_event_review_url(event):
    return reverse('events:review', kwargs={'slug': event.slug, 'pk': event.id.hex, 'token': event.auth_token})


def send_event_create_mail(event, moderators_email):

    current_site = Site.objects.get_current()
    extra_context = {'event': event, 'review_url': get_event_review_url(event),
                     'site_url': '{}://{}'.format(settings.SITE_SCHEME, current_site.domain)}

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
    extra_context = {'event': event, 'review_url': get_event_review_url(event),
                     'site_url': '{}://{}'.format(settings.SITE_SCHEME, current_site.domain)}

    # Send mail to moderators
    send_email('FOSSEvents | ' + event.name[:15] + ' updated!',
               'email/event_update_moderators_email.txt', moderators_email,
               extra_context, 'email/event_update_moderators_email.html')

    # Send mail to creator
    send_email('FOSSEvents | ' + event.name[:15] + ' updated!',
               'email/event_update_creator_email.txt', [event.owner_email],
               extra_context, 'email/event_update_creator_email.html')


def send_event_review_mail(review, moderator):

    # get all moderator's email
    moderators_email = User.objects.filter(Q(is_staff=True) | Q(is_moderator=True) |
                                           Q(is_superuser=True)).distinct().values_list('email', flat=True)

    current_site = Site.objects.get_current()
    extra_context = {'event': review.event, 'moderator': moderator, 'notes': review.comment,
                     'site_url': '{}://{}'.format(settings.SITE_SCHEME, current_site.domain)}

    # Send mail to moderators
    send_email('FOSSEvents | ' + review.event.name[:15] + ' reviewed!',
               'email/event_review_moderators_email.txt', moderators_email,
               extra_context, 'email/event_review_moderators_email.html')

    # Send mail to creator
    send_email('FOSSEvents | ' + review.event.name[:15] + ' reviewed!',
               'email/event_review_creator_email.txt', [review.event.owner_email],
               extra_context, 'email/event_review_creator_email.html')


def send_confirmation_mail(event, is_update=False):
    """
    Send mails about new event creation.

    :param event object
    :param is_update boolean
    """

    # get all moderator's email
    moderators_email = User.objects.filter(Q(is_staff=True) | Q(is_moderator=True) |
                                           Q(is_superuser=True)).distinct().values_list('email', flat=True)

    if is_update:
        return send_event_update_mail(event, moderators_email)

    return send_event_create_mail(event, moderators_email)


def create_event_review(moderator, event, data):
    """
    Update event with review data.

    :param moderator: User object
    :param event: Event object
    :param data: cleaned data dict
    :return: event review created object
    """
    data['moderator'] = moderator
    data['event'] = event

    review = models.EventReview.objects.create(**data)
    return review


def update_event_visibility(review):
    """
    Update event's `is_published` flag according to review

    :param review: EventReview object
    :return: event review updated object
    """
    review.event.is_published = False
    if review.is_approved:
        review.event.is_published = True

    review.event.save()
    return review
