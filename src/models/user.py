from flask.ext.sqlalchemy import SQLAlchemy
from flock import app

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	def __init__(self):
		pass
