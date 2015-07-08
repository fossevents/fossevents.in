from django.contrib.syndication.views import Feed
from .models import Event


class ArchiveFeed(Feed):
    title = 'fossevents.in'
    description = 'Seeing the light.....'
    link = '/archive/'

    def items(self):
        return Event.objects.filter(is_published=True)

    def item_link(self, item):
        return Event.get_absolute_url(item)

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return "Event Date : " + item.start_date.strftime('%Y-%m-%d %H:%M:%S') + " Event Page : " + item.homepage
