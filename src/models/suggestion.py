from flock import db, models.User

class Suggestion(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, foreign_key('user.id'))

	def __init__(self):
		pass
