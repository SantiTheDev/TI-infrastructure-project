import os
from sqlalchemy import create_engine
from decouple import config

db = create_engine(config['USER_DATABASE_URI'])
conn = db.connect()

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
