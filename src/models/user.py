
from flask.ext.sqlalchemy import SQLAlchemy
from flock import app

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    gmail = db.Column(db.String(120), unique=True)

	def __init__(self, gmail):
		self.gmail = gmail
