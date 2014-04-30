from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event_manager.models import Suggestion, SuggestionUser
from django.contrib.auth.models import User
from event_manager.forms import SuggestionForm
from django.core.urlresolvers import reverse


@login_required
def pending_suggestions(request):
	pass


@login_required
def my_suggestions(request):
	suggestion_users = SuggestionUser.objects.select_related().filter(user__id=request.user.id)
	suggestion_objects = [suggestion_user.suggestion for suggestion_user in suggestion_users] 
	suggestions = [
		{
			"id": suggestion.id,
		#	"user_name": request.user.username,
			"response": suggestion.response,
			"time": suggestion.time,
			"location_id": suggestion.location_id,
		#	"group_id": suggestion.group_id,
		} for suggestion in suggestion_objects
	]
	return render(request, 'suggestions.html', {'suggestions': suggestions})


@login_required
def new_suggestion(request):
	if request.method == POST:
		form = SuggestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('event_manager.views.my_suggestions'))
	else:
		form = SuggestionForm()
	
	return render(request, 'base.html', {'form': form})
