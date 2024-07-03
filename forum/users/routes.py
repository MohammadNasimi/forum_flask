from flask import Blueprint
from forum.users.models import User

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login')
def show():
    return "hello world"
