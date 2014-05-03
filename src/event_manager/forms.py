from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from event_manager.models import Suggestion, Event


class SuggestionForm(ModelForm):
	class Meta:
		model = Suggestion
		fields = ('location', 'users', 'time')
		
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields ('owner', 'invites', 'description', 'location', 'start_time')

	
class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.CharField(help_text="Please enter your email.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
