# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, editable=False)),
                ('modified', models.DateTimeField(auto_now=True, editable=False)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date', blank=True)),
                ('homepage', models.URLField(verbose_name='homepage', blank=True)),
                ('is_published', models.BooleanField(default=False, verbose_name='is published')),
                ('auth_token', models.CharField(max_length=100)),
                ('owner_email', models.EmailField(help_text='Email address of the submitter.', max_length=256, verbose_name="owner's email address")),
            ],
            options={
                'ordering': ('-start_date',),
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
