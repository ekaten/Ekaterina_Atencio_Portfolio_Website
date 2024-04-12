import os

class Config(object):
    RECAPTCHA_PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("SECRET_KEY")
