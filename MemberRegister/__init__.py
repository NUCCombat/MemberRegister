from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config.from_object('configuration')


db = SQLAlchemy(app)


from . import controller