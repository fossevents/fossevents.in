# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserQuerySet(models.QuerySet):
    def moderators(self):
        return self.filter(is_moderator=True)

    def email_users(self):
        return self.filter(is_moderator=True, is_superuser=True, is_staff=True)


class CustomUserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def moderators(self):
        return self.get_queryset().moderators()

    def email_users(self):
        return self.get_queryset().email_users()


class User(AbstractUser):

    is_moderator = models.BooleanField('active', default=False,
                                       help_text='Designates whether this user is a moderator or not')

    objects = CustomUserManager()

    def __str__(self):
        return self.username
