from os import urandom
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.database.models import db
from src.settings import config

DATABASE  = config["DATABASE"]
SECRET_KEY = config["SECRET_KEY"]

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///database/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app


from src import views