from flock import db

class Suggestion(db.Model):
	__tablename__ = 'suggestions'
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

