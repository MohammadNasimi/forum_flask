from forum.extensions import db
from forum.extensions import serializer_marshmall
from marshmallow import ValidationError
from flask_marshmallow import fields

class UserLogInSchema(serializer_marshmall.Schema):
    class Meta:
        fields = ('phone',)