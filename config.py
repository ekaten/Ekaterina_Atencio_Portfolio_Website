import os


class Config(object):
    RECAPTCHA_PUBLIC_KEY = os.environ.get('PUBLIC_KEY') or 'you-can-try-to-guess'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
