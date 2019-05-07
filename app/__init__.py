from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

app = Flask(__name__) #类实例
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#Flask-SQLAlchemy和Flask-Migrate初始化

#Flask-Login初始化
login = LoginManager(app)
login.login_view = 'login'

from app import routes,models
