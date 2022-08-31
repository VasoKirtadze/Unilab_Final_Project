import yagmail
import os


# print('email sent!')
# print(os.getenv('mypass'))
# print(os.environ.get('mypass'))


def send_mail(receiver, message):
    sender = 'vasokirtadze2@gmail.com'

    receiver = receiver

    subject = "Athlead"

    yag = yagmail.SMTP(user=sender, password="gjsqxrrfytukoduz")
    yag.send(to=receiver, subject=subject, contents=message)