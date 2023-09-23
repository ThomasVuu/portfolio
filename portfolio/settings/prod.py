from  .common import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['portfolio-ttcvu-6a79532e03f2.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config('DATABASE_URL')
}