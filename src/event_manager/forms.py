from django.forms import ModelForm
from event_manager.models import Suggestion


class SuggestionForm(ModelForm):
	class Meta:
		model = Suggestion
		fields = ['location', 'users', 'time']
