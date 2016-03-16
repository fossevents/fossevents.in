# -*- coding: utf-8 -*-


from django.contrib import admin
from reversion.admin import VersionAdmin

from . import models


@admin.register(models.Event)
class EventAdmin(VersionAdmin):
    list_display = ['name', 'owner_email', 'is_published', 'start_date', 'created']
    list_filter = ('is_published', 'created', 'start_date')
    search_fields = ('name', 'description', 'owner_email')
