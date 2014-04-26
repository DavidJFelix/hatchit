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
	events = [
		{
			"event_id": event.id,
			"event_owner": event.owner_id,
			"event_description": event.description,
			"event_location_id": event.location_id,
			"event_start_time": event.start_time,
			"event_end_time": event.end_time,
		} for event in event_objects
	]
	user_ids_mentioned = [event.get('event_owner') for event in events]
	users_mentioned = User.objects.filter(id__in=user_ids_mentioned)
	username_map = {user.id: user.username for user in users_mentioned}

	for event in events:
		event["event_owner_name"] = username_map.get(event.get("event_owner"))
		
	return render(request, 'events.html', {'events': events})
	
