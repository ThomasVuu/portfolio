from  .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-cr3c54fx4log@6x&&uuwd%m3!$3zd+nlaj+r436q91vs21ogt2'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
