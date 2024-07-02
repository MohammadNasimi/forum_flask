from forum import db


class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Datetime, defualt = db.fuc.current_timestamp())
