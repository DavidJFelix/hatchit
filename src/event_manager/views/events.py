from django.shortcuts import render
from event_manager.models import Event, Invite
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
