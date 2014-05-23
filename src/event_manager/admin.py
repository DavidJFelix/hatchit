from django.contrib import admin
from .models import Suggestion, Event, Invite, Location, SuggestionUser

# Register your models here.
admin.site.register(Suggestion)
admin.site.register(Event)
admin.site.register(Invite)
admin.site.register(Location)
admin.site.register(SuggestionUser)
