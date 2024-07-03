from flask import Flask
from .users.routes import users_blueprint
from .posts.routes import posts_blueprint
from forum.exceptions import resource_not_found,resource_sever_error
from forum.extensions import db,migrate

def register_error_handlers(app):
    app.register_error_handler(404,resource_not_found)
    app.register_error_handler(500,resource_sever_error)

app = Flask(__name__)


app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)
register_error_handlers(app)

app.config.from_object('config.developconfig')

db.init_app(app)
from .users.models import User # circular import
migrate.init_app(app, db)

# with app.app_context():
#     db.create_all() # set update model in database when run server
    


"""
    migrate database :
    1. flask --app forum.py db init -> create a migration repository, just one time run 
    2. flask --app forum.py db migrate -> create file for db models
    3. flask --app forum.py db upgrade -> add file model to db
"""