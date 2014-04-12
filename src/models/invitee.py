from flock import db

class Invitee(db.Model):
	
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

	def __init__(self):
		pass
