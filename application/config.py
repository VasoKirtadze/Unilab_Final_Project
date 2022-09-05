import os

dirname = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "VERy_Safe_Key"

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dirname, 'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
