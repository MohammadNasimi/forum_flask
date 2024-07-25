from flask import Blueprint,session
from flask.views import MethodView,View
from .serializer import UserLogInSchema,CodeSchema
from flask import request ,jsonify
from marshmallow import ValidationError
import random 
from datetime import datetime ,timedelta

from forum.extensions import db, sms_api
from .models import code,User

# jwt 
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token

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
        # check exist code in db for create or delete
        if bool(code.query.filter_by(phone=phone).first()):
            code_phone = code.query.filter_by(phone=phone).first()
            if not code_phone.expire_time < datetime.now():
                return jsonify({"message":"can't get code phone try again afew min ago"})
            else:
                db.session.delete(code_phone)
                db.session.commit()
                code_phone = code(
                            number=rand_num,
                            expire_time=datetime.now() + timedelta(minutes=10),
                            phone = phone
                            )
                db.session.add(code_phone)
                db.session.commit()
        else:
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



class CodePhoneView(View):
    def dispatch_request(self):
        code_ = request.get_json()
        schema = CodeSchema()
        try:
            valid_code = schema.load(code_)
        except ValidationError as err:
            # Handle validation errors
            return f"Error: {err}", 400
        def get_token(phone):
                phone_token = {"phone": phone}
                access_token = create_access_token(identity=phone_token,expires_delta = timedelta(minutes=10))
                refresh_token = create_refresh_token(identity=phone_token,expires_delta= timedelta(hours=2))
                return jsonify(access_token=access_token,refresh_token=refresh_token)
        
        # check correct code 
        code_phone = code.query.filter_by(phone=session.get('user_phone')).first()
        if code_phone.expire_time < datetime.now():
            return jsonify({"message":"Expiration Error, please try again"})
        if valid_code["number"] != str(code_phone.number):
            return jsonify({"message":"your code is wronge"})
        else:
            user = User.query.filter_by(phone=session.get('user_phone')).first()
            if not user:
                # Create user if not found
                new_user = User(phone=session.get('user_phone'))
                db.session.add(new_user)
                db.session.commit()
                return get_token(new_user)
            else:
                return get_token(user.phone)
        
@users_blueprint.route('/code',methods=['POST'])
def get_code():
    # This function is a wrapper for the view class instance
    return CodePhoneView.as_view('CodePhoneView')()