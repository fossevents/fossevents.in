# Third Party Stuff
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import render_to_string

current_site = Site.objects.get_current()


def send_mass_mail(subject_template_name, email_template_name,
                   context_list, html_email_template_name=None,
                   connection=None, request=None):
    """
    Sends mass django.core.mail.EmailMultiAlternatives to `to_email` provided in context_list.

     @param: email subject template as subject_template_name
     @param: email body text template as subject_template_name
     @param: data list each containing `context` and `to_email` as context_list
     @param: email body html template as html_email_template_name (optional)
     @param: smtp connection as connection (optional)
     @param: request for rendering template context as request (optional)
    """
    connection = connection or get_connection()
    messages = []
    for data in context_list:
        context = data.get('context')
        to_email = data.get('to_email')
        ctx_dict = {}
        if request is not None:
            ctx_dict = RequestContext(request, ctx_dict)
        # update ctx_dict after RequestContext is created
        # because template context processors
        # can overwrite some of the values like user
        # if django.contrib.auth.context_processors.auth is used
        if context:
            ctx_dict.update(context)
        ctx_dict.update({
            'site': current_site,
            'scheme': settings.SITE_SCHEME
        })
        subject = (render_to_string(subject_template_name, ctx_dict))
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
        message_txt = render_to_string(email_template_name,
                                       ctx_dict)

        email_message = EmailMultiAlternatives(subject, message_txt,
                                               from_email, [to_email])

        if html_email_template_name:
            try:
                message_html = render_to_string(
                    html_email_template_name, ctx_dict)
                email_message.attach_alternative(message_html, 'text/html')
            except TemplateDoesNotExist:
                pass
        messages.append(email_message)
    return connection.send_messages(messages)
