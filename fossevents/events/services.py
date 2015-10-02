# -*- coding: utf-8 -*-

from . import models


def get_public_event_listings(search_term=None):
    qs = models.Event.objects.filter(is_published=True)
    if search_term:
        qs = qs.filter(name__icontains=search_term)
    return qs
