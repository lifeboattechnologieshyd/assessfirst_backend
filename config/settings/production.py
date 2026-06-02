# ruff: noqa

from config.settings.common import *  # noqa : F403

ENABLE_EMAIL = True


DEBUG = False


############################
#       SILK SETTINGS      #
############################
ENABLE_SILK = False


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "assessfirst.ai",
    "www.assessfirst.ai",
]