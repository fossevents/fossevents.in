# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect, render

from . import models
from .decorators import match_token
from .forms import EventForm, EventReviewForm
from . import services


def event_detail(request, pk, slug=None, template_name='events/event_detail.html'):
    event = get_object_or_404(models.Event, pk=pk)
    if event.slug != slug:
        return redirect(event.get_absolute_url())
    ctx = {
        'event': event,
    }
    if not request.user.is_anonymous():
        if request.user.is_moderator or request.user.is_staff or request.user.is_superuser:
            ctx['review_url'] = services.get_event_review_url(event)
            ctx['form'] = EventReviewForm()

    return render(request, template_name, ctx)


@user_passes_test(lambda u: u.is_moderator or u.is_staff or u.is_superuser)
@login_required()
@require_http_methods(['POST'])
def event_review(request, pk, token, slug=None, event_detail_template='events/event_detail.html'):
    # TODO: Add reference in email for analytics
    # TODO: Add history of reviews in review page
    event = get_object_or_404(models.Event, pk=pk)
    if event.slug != slug:
        return redirect(event.get_absolute_url())

    form = EventReviewForm(data=request.POST)
    if form.is_valid():
        review = services.create_event_review(request.user, event, form.cleaned_data)
        services.update_event_visibility(review)
        services.send_event_review_mail(review, request.user)
        return HttpResponseRedirect(reverse('home'))

    ctx = {
        'event': event,
        'review_url': services.get_event_review_url(event),
        'form': form
    }
    return render(request, event_detail_template, ctx)


class EventCreateView(CreateView):
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        response = super().form_valid(form)
        services.send_confirmation_mail(self.object, False)
        return response


class EventUpdateView(UpdateView):
    form_class = EventForm
    template_name = 'events/event_form.html'
    queryset = models.Event.objects.all()

    @method_decorator(match_token)
    def dispatch(self, request, *args, **kwargs):
        return super(EventUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        response = super().form_valid(form)
        services.send_confirmation_mail(self.object, False)
        return response
