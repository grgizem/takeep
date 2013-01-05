from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context

from apps.event.models import Event, Participant


def send_joinrequest_mail(participant, event_id):
    event = Event.objects.get(id=event_id)

    sender = getattr(settings, 'EMAIL_HOST_USER', [])
    subject = "Request to join your event"
    recipients = [event.host.email]
    context = Context({'name': event.host.username,
             'participant_name': participant.username,
             'participant_id': participant.id,
             'event_title': event.title,
             'event_id': event.id,
             'site': Site.objects.get_current()})
    send_html_email(subject,
         sender,
         recipients,
         context,
         "event/mail/joinrequest")
    return True


def send_eventchange_mail(event_id):
    event = Event.objects.get(id=event_id)
    participants = Participant.objects.filter(event__id=event_id)
    
    sender = getattr(settings, 'EMAIL_HOST_USER', [])
    subject = "Event changed"
    recipients = []
    for participant in participants:
        recipients.append(participant.guest.email)
        context = Context({'name': participant.guest.username,
                 'event_title': event.title,
                 'event_id': event.id,
                 'site': Site.objects.get_current()})
        send_html_email(subject,
             sender,
             recipients,
             context,
             "event/mail/eventchange")
        recipients = []
    return True


def send_approval_mail(event_id, user_id):
    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)

    sender = getattr(settings, 'EMAIL_HOST_USER', [])
    subject = "Your attending request approved"
    recipients = [user.email]
    context = Context({'name': user.username,
             'event_title': event.title,
             'event_id': event.id,
             'site': Site.objects.get_current()})
    send_html_email(subject,
         sender,
         recipients,
         context,
         "event/mail/approval")
    return True


def send_disapproval_mail(event_id, user_id):
    event = Event.objects.get(id=event_id)
    user = User.objects.get(id=user_id)

    sender = getattr(settings, 'EMAIL_HOST_USER', [])
    subject = "Your attending request disapproved"
    recipients = [user.email]
    context = Context({'name': user.username,
             'event_title': event.title,
             'event_id': event.id,
             'site': Site.objects.get_current()})
    send_html_email(subject,
         sender,
         recipients,
         context,
         "event/mail/disapproval")
    return True


def send_cancellation_mail(event_id):
    event = Event.objects.get(id=event_id)
    participants = Participant.objects.filter(event__id=event_id)
    
    sender = getattr(settings, 'EMAIL_HOST_USER', [])
    subject = "Event cancelled"
    recipients = []
    for participant in participants:
        recipients.append(participant.guest.email)
        context = Context({'name': participant.username,
                 'event_title': event.title,
                 'event_id': event.id,
                 'site': Site.objects.get_current()})
        send_html_email(subject,
             sender,
             recipients,
             context,
             "event/mail/cancellation")
        recipients = []
    return True


def send_html_email(email_subject,
                    email_from, email_to,
                    email_context, email_template):
    plain_email = loader.get_template("%s.txt" % email_template)
    html_email = loader.get_template("%s.html" % email_template)
    plain_content = plain_email.render(email_context)
    html_content = html_email.render(email_context)
    msg = EmailMultiAlternatives(
        email_subject,
        plain_content,
        email_from,
        email_to
        )
    msg.attach_alternative(html_content, "text/html")
    return msg.send()