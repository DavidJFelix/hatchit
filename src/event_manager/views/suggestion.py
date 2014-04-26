from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event_manager.models import Suggestion
from django.contrib.auth.models import User

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
