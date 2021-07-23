from flask_mail import Message
from . import mail


def send_mail(content, recipients):
    msg = Message(content,
                  recipients=recipients)
    mail.send(msg)
