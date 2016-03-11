# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .views import homepage

urlpatterns = [
    url(r'^$', homepage, name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^privacy/$', TemplateView.as_view(template_name='privacy.html'), name="privacy"),
    url(r'^event/', include('fossevents.events.urls', namespace='events')),
]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
