# project/_config.py
import os
import psycopg2
import urlparse

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'pal.db'
CSRF_ENABLED = True
SECRET_KEY = '\xff\xdcUf\xdd\x9a\x9c\x16\x86\xaf\t\x8c\xc0\xce\x1b\xc4\x90*N\t\x04\x87z\x83'
DEBUG = False


# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

#SQLALCHEMY_DATABASE_URI = "postgresql://matt:Password@localhost/pal"
