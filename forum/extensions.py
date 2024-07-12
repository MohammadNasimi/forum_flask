from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from kavenegar import KavenegarAPI
import os 

from dotenv import load_dotenv

load_dotenv()

from flask_login import LoginManager
login_manager = LoginManager()

sms_api = KavenegarAPI(os.getenv("API_key_kave_negar"))

db = SQLAlchemy()
migrate = Migrate()
