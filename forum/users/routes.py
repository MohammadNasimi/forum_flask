from flask import Blueprint

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/login')
def show():
    return "hello world"
