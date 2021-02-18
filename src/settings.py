from os import urandom
from src import app
from src.database.models import db


DEBUG = True,
DATABASE = "db.sqlite",
SECRET_KEY = urandom(32)

app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///database/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.app = app
