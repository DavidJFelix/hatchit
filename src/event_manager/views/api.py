from django.shortcuts import render
import json
from django.http import HttpResponse
from event_manager.models import Suggestion, Event, Invite
from django.contrib.auth.models import User
from datetime import datetime

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


# TODO : Build add services for events, suggestions, invites seperately
def new(request):
		# event_description = request.POST["description"]
		# event_owner_id = request.POST["owner_id"]
		# event_location_id = request.POST["location_id"]

		event_description = "Felix"
		event_owner_id = 1
		event_location_id = 1
		event_start_time = datetime.now()
		event = Event(
			description = event_description,
			owner_id = event_owner_id,
			location_id = event_location_id,
			start_time = event_start_time
		)


		event.save()
		event_id = event.id

		invite_event_id = event_id
		invite_user_id = 1
		# invite_rsvp = "NONE"
		invite = Invite(
			event_id = invite_event_id,
			user_id = 1,
			rsvp = Invite.NONE
		)

		invite.save()

		return HttpResponse("ASDF", content_type="application/json")