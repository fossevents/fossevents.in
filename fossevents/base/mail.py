# Third Party Stuff
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string


def send_email(subject, email_template_name, to_emails,
               extra_context=None, html_email_template_name=None):
    ctx_dict = {}
    current_site = Site.objects.get_current()

    if extra_context:
        ctx_dict.update(extra_context)

    ctx_dict.update({
        'site': current_site,
        'scheme': settings.SITE_SCHEME
    })

    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
    message_txt = render_to_string(email_template_name,
                                   ctx_dict)

    email_message = EmailMultiAlternatives(subject, message_txt,
                                           from_email, to_emails)

    if html_email_template_name:
        try:
            message_html = render_to_string(
                html_email_template_name, ctx_dict)
            email_message.attach_alternative(message_html, 'text/html')
        except TemplateDoesNotExist:
            pass

    email_message.send()
