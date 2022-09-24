from flask import Flask
from api.users import db
from api.users.routes.users_bp import api_users


def create_app():
    app = Flask(__name__)

    app.config.from_object('config')

    db.init_app(app)

    app.register_blueprint(api_users)

