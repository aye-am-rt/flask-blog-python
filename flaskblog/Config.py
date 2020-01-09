import os

# in cmd >>> python >>> import secrets >>> secrets.token_hex(16)
#  >>> copy use paste random 16 bytes

class Config:
    SECRET_KEY = '40595f24c9c5560f4726bf8c2210099a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = "********@gmail.com"
    MAIL_PASSWORD = "*********"