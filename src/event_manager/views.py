from django.shortcuts import render
from event_manager.models import Suggestion, Event, Invite
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'login.html', {})

#FIXME: Remove comment when login works
#@login_required
def my_suggestions(request):
	#FIXME: Need to only select so many, also only yours
	suggestions = Suggestion.objects.values()
	return render(request, 'suggestions.html', {'suggestions': suggestions})
	
#FIXME: Remove comment when login works	
#@login_required
#def my_events(request, user_id='1'):
@login_required
def my_events(request):
	#FIXME: hardcoded user needs to go
	invites = Invite.objects.filter(user__id=request.user.id)
	event_objects = [invite.event for invite in invites]
	events = [event.get_dict() for event in event_objects]	
	return render(request, 'events.html', {'events': events})
	
