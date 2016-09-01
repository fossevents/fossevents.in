# -*- coding: utf-8 -*-
import uuid

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django_markdown.models import MarkdownField
from django_markdown.utils import markdown

from fossevents.base.models import TimeStampedUUIDModel
from fossevents.base.utils import get_date_diff_display


class Event(TimeStampedUUIDModel):
    """ Model to capture all details about the event.
    """
    name = models.CharField(blank=False, null=False, max_length=100, verbose_name=_("name"),)
    description = MarkdownField(blank=False, null=False, verbose_name=_("description"))
    start_date = models.DateTimeField(blank=False, verbose_name=_("start date"))
    end_date = models.DateTimeField(blank=True, verbose_name=_("end date"))
    homepage = models.URLField(blank=True, verbose_name=_("homepage"))
    is_published = models.BooleanField(blank=False, null=False, default=False, verbose_name=_("is published"))

    auth_token = models.CharField(blank=True, null=False, max_length=100)
    owner_email = models.EmailField(
        blank=False, null=False, max_length=256, verbose_name=_("owner's email address"),
        help_text=_("An email with the edit link for this event would be sent to this address. \
            Please provide a vaild address here."))

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ('-start_date', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'slug': self.slug, 'pk': self.id.hex})

    @property
    def slug(self):
        return slugify(self.name)

    # TODO: return date in localize timezone
    def date(self):
        return get_date_diff_display(self.start_date, self.end_date)

    @cached_property
    def description_html(self):
        return markdown(self.description)

    def save(self, *args, **kwargs):
        if not self.auth_token:
            self.auth_token = str(uuid.uuid4())
        super(Event, self).save(*args, **kwargs)
