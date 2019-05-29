from myblog.settings.common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']


# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['myblog-env.3giasrpd9x.us-east-1.elasticbeanstalk.com']

# configure the database
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

STATIC_ROOT = 'static'

