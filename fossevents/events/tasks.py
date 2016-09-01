# Third Party Stuff
from celery import shared_task

from .services import send_confirmation_mail


@shared_task
def send_aync_confirmation_email(event_id):
    send_confirmation_mail(event_id)
