from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from event_manager.models import Suggestion, SuggestionUser
from django.contrib.auth.models import User
from event_manager.forms import SuggestionForm
from django.core.urlresolvers import reverse

#FIXME: handle "pagination"
@login_required
def pending_suggestions(request):
	suggestion_users = list(
		SuggestionUser.objects\
		.select_related()\
		.filter(
			user_id=request.user.id,
			suggestion__response=Suggestion.NONE
		)\
		.order_by('-suggestion__time')
	)
	suggestions = [
		{
			#TODO:add elements
			"id": suggestion_user.suggestion.id,
			"response": suggestion_user.suggestion.response
		} for suggestion_user in suggestion_users
	]
	return render(request, 'suggestions.html',{'suggestions': suggestions})
	

#FIXME: handle "pagination"
@login_required
def my_suggestions(request):
	suggestions = [
		{
			"id": suggestion.id,
			"response": suggestion.response
		} for suggestion in Suggestion.objects\
			.prefecth_related()\
			.filter(owner_id=request.user.id)
	]
	return render(request, 'suggestions.html', {'suggestions': suggestions})


@login_required
def add_suggestion(request):
	if request.method == POST:
		form = SuggestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('event_manager.views.my_suggestions'))
	else:
		form = SuggestionForm()
	
	return render(request, 'base.html', {'form': form})
