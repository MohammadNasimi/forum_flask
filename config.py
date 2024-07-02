import os
from dotenv import load_dotenv

load_dotenv()

class config():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CSRF_ENABLED = True
    CSRF_SSESION_KEY= os.getenv("CSRF_SSESION_KEY")
    SECRET_KEY= os.getenv("SECRET_KEY")

class productconfig(config):
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = ...
    
    
class developconfig(config):
    DEBUG =False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(config.BASE_DIR,'forum.db')