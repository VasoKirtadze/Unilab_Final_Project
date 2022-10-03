from flask_mail import Message
from application.extensions import mail
from threading import Thread

def send_mail(subject, receiver, html):

    msg = Message(subject=subject, html=html, recipients=[receiver], sender="AthLead")
    thread = Thread(target=mail.send(msg))
    thread.start()
