from flask import Blueprint
from api.users.controllers.UserController import get_user, delete_user, update_user, create_user


api_users = Blueprint('apiUsers', __name__, url_prefix='api/users')


@api_users.route('/create', ['POST'])
def store():
    return create_user()


@api_users.route('/<int:user_id>', ['GET'])
def get(user_id):
    return get_user(user_id)


@api_users.route('/<int:user_id>', ['POST'])
def update(user_id):
    return update_user(user_id)


@api_users.route('/<int:user_id>/delete', ['DELETE'])
def delete(user_id):
    return delete_user(user_id)


