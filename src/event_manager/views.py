from django.shortcuts import render
from event_manager.models import Suggestion, Event
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'login2.html', {})

#FIXME: Remove comment when login works
#@login_required
def my_suggestions(request):
	#FIXME: Need to only select so many, also only yours
	suggestions = Suggestion.objects.values()
	return render(request, 'suggestions.html', suggestions)
	
#FIXME: Remove comment when login works	
#@login_required
def my_events(request):
	#FIXME: Need to only select so many, also only yours
	events = Event.objects.values()
	return render(request, 'events.html', events)
	
