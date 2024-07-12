from forum.database import BaseModel
from forum.extensions import db,login_manager


from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(BaseModel,UserMixin):
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