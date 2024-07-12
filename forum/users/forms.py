from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import ValidationError
from .models import User,code




class UserRegistrationForm(FlaskForm):
    phone = StringField("phone")
    
    def vaidate_phoen(self,phone):
        codes = code.query.filter_by(phone = phone.data)
        if codes:
            code.query.filter_by(phone = phone.data).delete()
        user = User.query.filter_by(phone = phone.data).first()
        if user:
            raise ValidationError("this phone exists")
        
        
class UserCodeVerifyForm(FlaskForm):
    code = StringField("code")