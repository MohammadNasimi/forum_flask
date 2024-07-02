from forum.database import BaseModel
from forum import db

class User(BaseModel):
    phone = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        return f'phone {self.phone}'