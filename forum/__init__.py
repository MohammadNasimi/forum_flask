from flask import Flask
from .posts.routes import posts_blueprint
from .users.routes import users_blueprint
from forum.exceptions import resource_not_found,resource_sever_error
from forum.extensions import db,migrate,serializer_marshmall
from forum.users.models import User,code

def register_error_handlers(app):
    app.register_error_handler(404,resource_not_found)
    app.register_error_handler(500,resource_sever_error)

def register_shell_context(app):
	def shell_context():
		return {
			'db': db,
			'User': User,
			'Code': code,
		}
	app.shell_context_processor(shell_context)

app = Flask(__name__)


app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)
register_error_handlers(app)
register_shell_context(app)

app.config.from_object('config.developconfig')

db.init_app(app)
# import models 
from .users.models import User # circular import
migrate.init_app(app, db)
serializer_marshmall.init_app(app)
# with app.app_context():
#     db.create_all() # set update model in database when run server
    
# @app.before_request
# def before_request():
# 	print('This is before any request')

# @app.after_request
# def after_request(response):
# 	print('This is after any request')
# 	print(response)
# 	return response   # middleware

"""
    migrate database :
    1. flask --app forum.py db init -> create a migration repository, just one time run 
    2. flask --app forum.py db migrate -> create file for db models
    3. flask --app forum.py db upgrade -> add file model to db
    
    # run flask 
    flask --app run.py run
"""