# -*- coding: utf-8 -*-

from . import models


def get_public_event_listings():
    qs = models.Event.objects.filter(is_published=True)
    return qs
