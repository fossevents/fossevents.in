# Third Party Stuff
from django.conf.urls import url

from .views import EventCreateView

urlpatterns = [
    url(r'^add/$', EventCreateView.as_view(), name="event-create"),
]
