from django.db import models


class Suggestion(models.Model):
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
	
	#user=
	response = models.CharField(
		max_length=1,
		choices=RESPONSE_CHOICES,
		default=NONE)
	#suggestion_type=
	time = models.DateTime(
		null=True,
		blank=True
	)
	#location=
	#group=
	#activity=

	
class Event(models.Model):
	#owner=
	#invites=
	description = models.TextField()
	#location=
	start_time = models.DateTime()
	end_time = models.DateTime(
		null=True,
		blank=True
	)


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
	#event
	#user
	rsvp = models.CharField(
		max_length=2,
		choices=RSVP_CHOICESm
		default=NONE)
		
