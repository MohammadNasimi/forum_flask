from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from kavenegar import KavenegarAPI
import os 

from dotenv import load_dotenv

load_dotenv()

# serializer package
from flask_marshmallow import Marshmallow

sms_api = KavenegarAPI(os.getenv("API_key_kave_negar"))

db = SQLAlchemy()
migrate = Migrate()
serializer_marshmall = Marshmallow()
