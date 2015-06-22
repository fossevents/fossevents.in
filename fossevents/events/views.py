# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render, get_object_or_404

from . import models


def event_detail(request, pk, slug=None, template='pages/event_detail.html'):
    event = get_object_or_404(models.Event, pk=pk)
    ctx = {
        'event': event,
    }
    return render(request, template, ctx)
