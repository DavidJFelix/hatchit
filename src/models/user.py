from flock import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	suggestions = db.relationship('suggestion', secondary=suggestions,
		backref=db.backref('users', lazy='dynamic'))

	def __init__(self):
		pass
