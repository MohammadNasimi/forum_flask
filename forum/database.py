from forum import db
import datetime

class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now)
    update_at = db.Column(db.DateTime, default = datetime.datetime.now,
                          onupdate = datetime.datetime.now)
