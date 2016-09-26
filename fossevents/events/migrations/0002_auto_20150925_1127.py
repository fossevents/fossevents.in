# -*- coding: utf-8 -*-


from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=django_markdown.models.MarkdownField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='event',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='event',
            name='owner_email',
            field=models.EmailField(help_text='An email with the edit link for this event would be sent to this address.             Please provide a vaild address here.', max_length=256, verbose_name="owner's email address"),
        ),
    ]
