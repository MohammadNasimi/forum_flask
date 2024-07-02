from flask import Flask
from .users.routes import users_blueprint
from .posts.routes import posts_blueprint
from flask_sqlalchemy import SQLAlchemy
from forum.exceptions import resource_not_found,resource_sever_error

def register_error_handlers(app):
    app.register_error_handler(404,resource_not_found)
    app.register_error_handler(500,resource_sever_error)

app = Flask(__name__)


app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)
register_error_handlers(app)

app.config.from_object('config.developconfig')

db = SQLAlchemy(app)

from .users.models import User # circular import

with app.app_context():
    db.create_all() # set update model in database when run server
    
