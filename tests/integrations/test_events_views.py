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


def test_event_create(client, mocker):
    url = reverse('event-create')

    data = {
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }

    response = client.post(url, data)
    assert response.status_code == 302


def test_event_create_without_url_scheme(client, mocker):
    url = reverse('event-create')

    data = {
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '2016-08-12 21:00',
        'end_date': '2016-08-13 18:00',
        'homepage': 'example.com',
        'owner_email': 'test@example.com'
    }

    response = client.post(url, data)
    assert response.status_code == 302


EventErrorCasesData = [
    ({}, 'name'),
    ({
        # Name required field
        'name': '',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }, 'name'),
    ({
        # Description required field
        'name': 'Event01',
        'description': '',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }, 'description'),
    ({
        # Start date required field
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': 'test@example.com'
    }, 'start_date'),
    ({
         # End date required field
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'end_date'),
    ({
         # Format of start date
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '12-08-2016',
         'end_date': '2016-08-13',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'start_date'),
    ({
         # Format of end date
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '13-08-2016',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'end_date'),
    ({
         # End date should be greater than start date
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '2016-08-11',
         'homepage': 'http://example.com',
         'owner_email': 'test@example.com'
     }, 'end_date'),
    ({
         # Invalid url
         'name': 'Event01',
         'description': 'Event01 description',
         'start_date': '2016-08-12',
         'end_date': '2016-08-11',
         'homepage': 'example',
         'owner_email': 'test@example.com'
     }, 'homepage'),
    ({
        # Owner email required field
        'name': 'Event01',
        'description': 'Event01 description',
        'start_date': '2016-08-12',
        'end_date': '2016-08-13',
        'homepage': 'http://example.com',
        'owner_email': ''
    }, 'owner_email'),
]


@pytest.mark.parametrize("test_data,error_field", EventErrorCasesData)
def test_event_create_error(test_data, error_field, client):
    url = reverse('event-create')
    response = client.post(url, test_data)
    assert response.status_code == 200
    assert len(response.context['form'][error_field].errors)
