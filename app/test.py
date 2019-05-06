from werkzeug.security import generate_password_hash
from app.models import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)


db = SQLAlchemy(app)
db.create_all()

