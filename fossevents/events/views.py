# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404, redirect, render

from . import models


def event_detail(request, pk, slug=None, template_name='events/event_detail.html'):
    event = get_object_or_404(models.Event, pk=pk)
    if event.slug != slug:
        return redirect(event.get_absolute_url())
    ctx = {
        'event': event,
    }
    return render(request, template_name, ctx)
