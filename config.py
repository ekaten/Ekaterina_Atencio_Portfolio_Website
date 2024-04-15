import os
from dotenv import dotenv_values

config = dotenv_values(".env")
print(config)


class Config(object):
    RECAPTCHA_PUBLIC_KEY = config['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = config['RECAPTCHA_PRIVATE_KEY']
    # RECAPTCHA_PUBLIC_KEY = "6Lf-ULkpAAAAAFumGAt9LmenYSyNjOkgw68sMNAJ"
    # RECAPTCHA_PRIVATE_KEY = "6Lf-ULkpAAAAAJGAsqeWIP_j3KPe6JBaO2aUMHX7"


test = Config()
print(test.RECAPTCHA_PUBLIC_KEY)
print(test.RECAPTCHA_PRIVATE_KEY)



