# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    is_moderator = models.BooleanField('active', default=False,
                                       help_text='Designates whether this user is a moderator or not')

    def __str__(self):
        return self.username
