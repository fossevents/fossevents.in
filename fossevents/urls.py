# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [

    # Django Admin (Comment the next line to disable the admin)
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('fossevents.pages.urls', namespace='pages')),
    url(r'^event/', include('fossevents.events.urls', namespace='events')),

    url('^markdown/', include('django_markdown.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
