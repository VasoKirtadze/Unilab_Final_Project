import os

class Config(object):

    dirname = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = "VERy_Safe_Key"

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dirname, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '1d894265aa1b89'
    MAIL_PASSWORD = 'ca9a347794134d'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False