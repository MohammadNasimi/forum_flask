from flask import Blueprint
from flask.views import MethodView
from .serializer import UserLogInSchema
from flask import request ,jsonify
from forum.extensions import serializer_marshmall

users_blueprint = Blueprint('users', __name__)


class LogInView(MethodView):
    
    def get(self):
        return jsonify({"hi":"how adk"})

    def post(self):
        # instead request.form --> request.get_json()
        data = request.get_json()
        print(data.get("phone"," "))
        return f'phone: {data}'
    
@users_blueprint.route('/login',methods=['GET', 'POST'])
def log_in():
    # This function is a wrapper for the view class instance
    return LogInView.as_view('log_in')()