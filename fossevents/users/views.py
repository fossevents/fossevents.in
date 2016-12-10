from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import login as django_login
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect


def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    return django_login(request, template_name='users/login.html', *args, **kwargs)


def logout(request, *args, **kwargs):
    auth_logout(request)
    return HttpResponseRedirect(reverse('users:login'))
