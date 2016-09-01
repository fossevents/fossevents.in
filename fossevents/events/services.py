# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from fossevents.base.mail import send_mass_mail

from . import models

User = get_user_model()


def get_public_event_listings(search_term=None):
    qs = models.Event.objects.filter(is_published=True)
    qs = qs.order_by('-start_date')
    if search_term:
        qs = qs.filter(name__icontains=search_term)
    return qs


def send_mail_to_moderators(users, event):

    # all mails data list
    context_list = list()

    for user in users:
        # get senders from invitation objects
        data = {
            'context': {
                'user': user,
                'event': event,
                'event_link': ''
            },
            'to_email': user.email
        }

        # add mail message to mass mail list
        context_list.append(data)

    send_mass_mail('email/event_moderators_email_subject.txt',
                   'email/event_moderators_email.txt', context_list,
                   'email/event_moderators_email.html')


def send_mail_to_creator(event):
    data = {
        'context': {
            'event': event,
            'event_link': ''
        },
        'to_email': event.owner_email
    }

    send_mass_mail('email/event_creator_email_subject.txt',
                   'email/event_creator_email.txt', [data],
                   'email/event_creator_email.html')


def send_confirmation_mail(event_id):
    """
    Send mails about new event creation.
    """
    event = models.Event.objects.get(id=event_id)

    # get all end users both candidates and employers
    users = User.objects.filter(is_staff=True)

    send_mail_to_moderators(users, event)
    send_mail_to_creator(event)
    return
