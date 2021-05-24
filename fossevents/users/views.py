from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth import views as auth_views


def logout(request, *args, **kwargs):
    auth_logout(request)
    return HttpResponseRedirect(reverse('users:login'))
