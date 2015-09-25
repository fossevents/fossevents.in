# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import reversion
from django.contrib import admin

from . import models


@admin.register(models.Event)
class EventAdmin(reversion.VersionAdmin):
    list_display = ['name', 'owner_email', 'is_published', 'start_date', 'created']
    list_filter = ('is_published', 'created', 'start_date')
    search_fields = ('name', 'description', 'owner_email')
