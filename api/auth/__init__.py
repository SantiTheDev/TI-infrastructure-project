import os
from sqlalchemy import create_engine
from decouple import config
from flask_httpauth import HTTPBasicAuth


db = create_engine(config['AUTH_DATABASE_URI'])
conn = db.connect()
basedir = os.path.abspath(os.path.dirname(__file__))
