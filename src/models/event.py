from flock import db

class Event(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

	def __init__(self):
		pass
