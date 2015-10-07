import pytest
from ..factories import EventFactory

pytestmark = pytest.mark.django_db


def test_rss_feed_url(client):
    url = '/feed/rss/'
    response = client.get(url)
    assert response.status_code == 200

    url = '/feed/rss/latest'
    response = client.get(url)
    assert response.status_code == 404


def test_rss_feed(client):
    url = '/feed/rss/'
    sample_event = EventFactory.create(is_published=True)
    sample_event.save()
    response = client.get(url)
    assert sample_event.description in response.content
