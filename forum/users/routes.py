from flask import Blueprint
from flask.views import MethodView
from .serializer import UserLogInSchema
from flask import request ,jsonify
from marshmallow import ValidationError


users_blueprint = Blueprint('users', __name__)


class LogInView(MethodView):
    
    def get(self):
        return jsonify({"hi":"how adk"})

    def post(self):
        # check correct data
        # instead request.form --> request.get_json()
        data = request.get_json()
        schema = UserLogInSchema()
        try:
            schema.load(data)
        except ValidationError as err:
            # Handle validation errors
            return f"Error: {err}", 400
        
        # print(data.get("phone"," "))
        return f'phone: {data}',200
    
@users_blueprint.route('/login',methods=['GET', 'POST'])
def log_in():
    # This function is a wrapper for the view class instance
    return LogInView.as_view('log_in')()