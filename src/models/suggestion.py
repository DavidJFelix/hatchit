from flock import db

class Suggestion(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self):
		pass
