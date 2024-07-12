from flask import Blueprint
from flask.views import View
from .serializer import UserLogInSchema
from flask import request ,jsonify

users_blueprint = Blueprint('users', __name__)


class LogInView(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        if request.method == "GET":
            return jsonify({"hi":"how adk"})
        elif request.method == "POST":
            print(request.form)
            return jsonify({"hi":"how adk"})
@users_blueprint.route('/login')
def log_in():
    # This function is a wrapper for the view class instance
    return LogInView.as_view('log_in')()