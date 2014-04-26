from django.shortcuts import render
import json
from django.http import HttpResponse
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

"""def login_user(request):
	username = password = ""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				#login(re
				pass

"""

def my_events_json(request):
	invites = Invite.objects.select_related().filter(user__id=1)
	event_objects = [invite.event for invite in invites]
	events = [
		{
			"id": event.id,
			"owner_name": event.owner.username,
			"description": event.description,
			"location_id": event.location_id,
			"start_time": str(event.start_time),
			"end_time": str(event.end_time),
		} for event in event_objects
	]
	return HttpResponse(json.dumps(events), content_type="application/json")
	
def api_get(request, type="e"):
		if type == "e":
			# data = Event.objects.values()
			# return render(request, 'api.html', {'data': data})
			invites = Invite.objects.select_related().filter(user__id=1)
			event_objects = [invite.event for invite in invites]
			events = [
				{
					"id": event.id,
					"owner_name": event.owner.username,
					"description": event.description,
					"location_id": event.location_id,
					"start_time": str(event.start_time),
					"end_time": str(event.end_time),
				} for event in event_objects
			]
			return HttpResponse(json.dumps(events), content_type="application/json")

		elif type == "u":
			Users = User.objects.all()
			data = [
				{
					"id": user.id,
					"username": user.username,
					"first_name": user.first_name,
					"last_name": user.last_name,
					"email": user.email
				} for user in Users
			]
			return HttpResponse(json.dumps(data), content_type="application/json")

		elif type == "s":
			Suggestions = Suggestion.objects.all()
			data = [
				{
					"id": suggestion.id,
					"username": suggestion.user_id,
					"first_name": suggestion.response,
					"last_name": str(suggestion.time)
				} for suggestion in Suggestions
			]
			return HttpResponse(json.dumps(data), content_type="application/json")

		else:
			return render(request, 'api.html', {'data': ""})


