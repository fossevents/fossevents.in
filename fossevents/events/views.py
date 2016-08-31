# -*- coding: utf-8 -*-


from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from .forms import EventCreateForm


def event_detail(request, pk, slug=None, template_name='events/event_detail.html'):
    event = get_object_or_404(models.Event, pk=pk)
    if event.slug != slug:
        return redirect(event.get_absolute_url())
    ctx = {
        'event': event,
    }
    return render(request, template_name, ctx)


class EventCreateView(CreateView):
    form_class = EventCreateForm
    template_name = 'events/event_create.html'
