from .services import send_confirmation_mail


class SendMailPostSaveMixin(object):

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        response = super(SendMailPostSaveMixin, self).form_valid(form)
        send_confirmation_mail(self.object)
        return response
