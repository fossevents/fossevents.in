import pytest
from django.core.urlresolvers import reverse
from .. import factories as f

pytestmark = pytest.mark.django_db


def test_homepage(client):
    event = f.EventFactory(is_published=False)
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    # should have 'events' in the template context
    assert 'events' in response.context

    # should not display any event, if none are published
    assert len(response.context['events']) == 0

    # should now contain one event, after it's published
    event.is_published = True
    event.save()
    response = client.get(url)
    assert len(response.context['events']) == 1


def test_event_create(client):
    url = reverse('event-create')

    # Error on blank data
    response = client.post(url, {})
    assert response.status_code == 200

    data = {
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-11',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }

    # End date should be greater than start date
    response = client.post(url, data)
    assert response.status_code == 200

    data['end_date'] = '2016-08-13'
    response = client.post(url, data)
    assert response.status_code == 302
