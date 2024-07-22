from forum.extensions import db
from forum.extensions import serializer_marshmall
from marshmallow import ValidationError
from flask_marshmallow import fields
from .models import User,code
class UserLogInSchema(serializer_marshmall.Schema):
    class Meta:
        model = User
        fields = ('phone',)
        
class CodeSchema(serializer_marshmall.Schema):
    class Meta:
        model = code
        fields = ('number',)