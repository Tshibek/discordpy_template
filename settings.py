import os
import json
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
secrets = json.loads(open(os.path.join(BASE_DIR, 'secret.json')).read())


DATABASES = {
    'default': {
        # Database driver
        'ENGINE': 'django.db.backends.sqlite3',
        # Replace below with Database Name if using other database engines
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# If you want have all model in one models.py use only DB
INSTALLED_APPS = (
    'db',
    # 'core.admin',
    # 'core.example'
)

"""
To connect to an existing postgres database, first:
pip install django psycopg2
then overwrite the settings above with:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = secrets['secret_key']



#For Bot
TOKEN = secrets['discord_token']
BotStatus = secrets['bot_status']
Prefix = secrets['discord_prefix']
