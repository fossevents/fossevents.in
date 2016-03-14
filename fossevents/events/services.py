# -*- coding: utf-8 -*-

from . import models


def get_public_event_listings(search_term=None):
    qs = models.Event.objects.filter(is_published=True)
    qs = qs.order_by('-start_date')
    if search_term:
        qs = qs.filter(name__icontains=search_term)
    return qs
