# -*- coding: utf-8 -*-


from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .events.views import event_detail
from .views import homepage

uuid_regex = '[a-fA-F0-9]{8}-?[a-fA-F0-9]{4}-?[1345][a-fA-F0-9]{3}-?[a-fA-F0-9]{4}-?[a-fA-F0-9]{12}'

urlpatterns = [
    url(r'^$', homepage, name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^privacy/$', TemplateView.as_view(template_name='privacy.html'), name="privacy"),
    url(r'^(?P<slug>[-\w]+)-(?P<pk>%s)/$' % uuid_regex, event_detail, name="event-detail"),
]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [url(r'^devrecargar/', include('devrecargar.urls', namespace='devrecargar'))]
