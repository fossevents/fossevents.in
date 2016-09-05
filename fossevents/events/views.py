# -*- coding: utf-8 -*-

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from .decorators import match_token
from .forms import EventForm
from .mixins import SendMailPostSaveMixin


def event_detail(request, pk, slug=None, template_name='events/event_detail.html'):
    event = get_object_or_404(models.Event, pk=pk)
    if event.slug != slug:
        return redirect(event.get_absolute_url())
    ctx = {
        'event': event,
    }
    return render(request, template_name, ctx)


class EventCreateView(SendMailPostSaveMixin, CreateView):
    form_class = EventForm
    template_name = 'events/event_form.html'


class EventUpdateView(SendMailPostSaveMixin, UpdateView):
    form_class = EventForm
    template_name = 'events/event_form.html'
    queryset = models.Event.objects.all()

    @method_decorator(match_token)
    def dispatch(self, request, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(request, *args, **kwargs)
