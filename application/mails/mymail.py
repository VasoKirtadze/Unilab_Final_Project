import yagmail
import os


def send_mail(receiver, message):
    sender = 'vasokirtadze2@gmail.com'

    receiver = receiver

    subject = "Athlead"

    yag = yagmail.SMTP(user=sender, password="gjsqxrrfytukoduz")
    yag.send(to=receiver, subject=subject, contents=message)