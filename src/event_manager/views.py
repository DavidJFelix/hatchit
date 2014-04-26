from django.shortcuts import render
from event_manager.models import Suggestion, Event, Invite
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'login.html', {})

@login_required
def my_suggestions(request):
	suggestion_objects = Suggestion.objects.select_related().filter(user__id=request.user.id)
	suggestions = [
		{
			"id": suggestion.id,
			"user_name": suggestion.user.username,
			"response": suggestion.response,
			"time": suggestion.time,
			"location_id": suggestion.location_id,
			"group_id": suggestion.group_id,
		} for suggestion in suggestion_objects
	]
	return render(request, 'suggestions.html', {'suggestions': suggestions})
	
@login_required
def my_events(request):
	invites = Invite.objects.select_related().filter(user__id=request.user.id)
	event_objects = [invite.event for invite in invites]
	events = [
		{
			"id": event.id,
			"owner_name": event.owner.username,
			"description": event.description,
			"location_id": event.location_id,
			"start_time": event.start_time,
			"end_time": event.end_time,
		} for event in event_objects
	]
	return render(request, 'events.html', {'events': events})
	
