from forum.database import BaseModel
from forum.extensions import db




class User(BaseModel):
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    is_active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f'phone {self.phone}'
    
    
class code(BaseModel):
    code = db.Column(db.Integer)
    expire_time = db.Column(db.DateTime,nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)

    def __repr__(self):
        return f'phone {self.phone}, code {self.code}'