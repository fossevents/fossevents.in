import pytest

pytestmark = pytest.mark.django_db


def test_rss_feed_url(client):
    urls = ['/feed/rss.xml', '/feed/atom.xml']
    for url in urls:
        response = client.get(url)
        assert response.status_code == 200


def test_url_is_present_pages(client):
    response = client.get('/')
    assert '<link type="application/atom+xml"' in response.content.decode('utf-8')
    assert '<link type="application/rss+xml"' in response.content.decode('utf-8')
