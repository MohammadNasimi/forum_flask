from flask import Blueprint

posts_blueprint = Blueprint('posts', __name__)


@posts_blueprint.route('/')
def show():
    return "hello posts"
