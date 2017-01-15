# project/_config.py
import os
import urlparse

import psycopg2

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
