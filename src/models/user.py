from flock import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column('user_id', db.Integer, primary_key=True)

	def __init__(self):
		pass
