import pytest
from django.urls import reverse
from .. import factories as f

pytestmark = pytest.mark.django_db


def test_login(client):
    user = f.UserFactory()
    url = reverse('users:login')

    # test login page
    response = client.get(url)
    assert response.status_code == 200

    data = {
        'username': user.username,
        'password': 'test'
    }

    response = client.post(url, data)
    assert response.status_code == 302


def test_logout(client):
    url = reverse('users:logout')

    client.login()

    response = client.get(url)
    assert response.status_code == 302
    assert 'login' in response.url
