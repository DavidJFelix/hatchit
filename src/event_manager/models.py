from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
	x = models.DecimalField(
		max_digits=10,
		decimal_places=5
	)
	y = models.DecimalField(
		max_digits=10,
		decimal_places=5
	)
	
	def __str__(self):
		return "x:" + str(self.x) + ", y:" + str(self.y)

class Suggestion(models.Model):
	time = models.DateTimeField(
		null=True,
		blank=True
	)
	location = models.ForeignKey(
		Location,
		null=True,
		blank=True
	)
	owner = models.ForeignKey(
		User,
		related_name='owner'
	)
	users = models.ManyToManyField(User, through='SuggestionUser')
	activity = models.CharField(
		max_length=50,
		blank=True
	)
	
	def __str__(self):
		return str(self.owner) + ":" str(self.activity) + " @ " + str(self.location) + ", " + str(self.time)

class SuggestionUser(models.Model):
	YES = 'Y'
	NO = 'N'
	MAYBE = 'M'
	NONE = 'O'
	RESPONSE_CHOICES = (
		(YES, 'Yes'),
		(NO, 'No'),
		(MAYBE, 'Maybe'),
		(NONE, 'No vote'),
	)
	
	response = models.CharField(
		max_length=1,
		choices=RESPONSE_CHOICES,
		default=NONE)
	user = models.ForeignKey(User)
	suggestion = models.ForeignKey(Suggestion)
	
	def __str__(self):
		return str(self.user) + ":" + str(self.suggestion)

class Event(models.Model):
	owner = models.ForeignKey(
		User,
		related_name='owner'
	)
	invites = models.ManyToManyField(User, through='Invite')
	description = models.TextField()
	location = models.ForeignKey(Location)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField(
		null=True,
		blank=True
	)
	
	def __str__(self):
		return str(self.owner) + ":" str(self.location) + "@" + str(self.start_time)


class Invite(models.Model):
	YES = 'Y'
	NO = 'N'
	MAYBE_YES = 'MY'
	MAYBE_NO = 'MN'
	NONE = 'O'
	RSVP_CHOICES = (
		(YES, 'Yes'),
		(NO, 'No'),
		(MAYBE_YES, 'Maybe Yes'),
		(MAYBE_NO, 'Maybe No'),
		(NONE, 'No response'),
	)
	event = models.ForeignKey(Event)
	user = models.ForeignKey(User)
	rsvp = models.CharField(
		max_length=2,
		choices=RSVP_CHOICES,
		default=NONE
	)
	
	def __str__(self):
		return str(user) + ":" + str(event)
	
