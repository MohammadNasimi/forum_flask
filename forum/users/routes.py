from flask import Blueprint,session
from flask.views import MethodView
from .serializer import UserLogInSchema
from flask import request ,jsonify
from marshmallow import ValidationError
import random 
from datetime import datetime ,timedelta

from forum.extensions import db, sms_api
from .models import code


users_blueprint = Blueprint('users', __name__)


class LogInView(MethodView):
    
    def get(self):
        user_phone = session.get('user_phone',None)
        return jsonify({"log in this phone":f"{user_phone}"})

    def post(self):
        # check correct data
        # instead request.form --> request.get_json()
        data = request.get_json()
        schema = UserLogInSchema()
        try:
            valid_data = schema.load(data)
        except ValidationError as err:
            # Handle validation errors
            return f"Error: {err}", 400
        # create code 
        rand_num = random.randint(1000, 9999)
        phone = valid_data.get("phone"," ")
        session['user_phone'] = phone
        # params = {'sender':'', 'receptor':int(phone), 'message':rand_num}
        # sms_api.sms_send(params)
        print(rand_num)
        code_phone = code(
                    number=rand_num,
                    expire_time=datetime.now() + timedelta(minutes=10),
                    phone = phone
                    )
        db.session.add(code_phone)
        db.session.commit()
        return jsonify({"message":f"send code to phone -> {phone}"})

        
        
@users_blueprint.route('/login',methods=['GET', 'POST'])
def log_in():
    # This function is a wrapper for the view class instance
    return LogInView.as_view('log_in')()