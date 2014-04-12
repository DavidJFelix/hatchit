from flock import db

class Invitee(db.Model):
	__tablename__ = 'invitees'
	event_id = db.Column(db.Integer, db.ForeignKey('event.id'), primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
	user = relationship('User', backref='invitation')
	event = relationship('Event', backref='invitation')

