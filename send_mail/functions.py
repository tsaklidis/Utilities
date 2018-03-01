#  In order to use this function you have to create a Django project
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives


def send_custom_mail(ctx, subject_path, template_path, recipients):
    # recipients must be list (array) ['info@example.com']
    # settings.FROM u'S.I.Tsaklidis <techsupport@tsaklidis.gr'

    text_content = u''
    if 'False' in recipients:
        recipients.remove('False')

    template = get_template(template_path, using='django')
    context = Context(ctx)
    subject = render_to_string(subject_path, ctx, using='django')

    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    content = template.render(context)
    message = EmailMultiAlternatives(
        subject, text_content,
        settings.FROM, recipients)
    message.attach_alternative(content, 'text/html')
    message.content_subtype = "html"
    message.send()
