# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404, render


from . import models


def event_detail(request, pk, slug=None, template_name='pages/event_detail.html'):
    event = get_object_or_404(models.Event, pk=pk)
    ctx = {
        'event': event,
    }
    return render(request, template_name, ctx)
