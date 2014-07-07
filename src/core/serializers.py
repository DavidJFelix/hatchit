from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Invite, Suggestion, Location


class EventSerializer(serializers.HyperLinkedModelSerializer):
	
	class Meta:
		model = Event


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Idea

class InviteSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Invite


class LocationSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Location
		fields = ('url', 'x', 'y')

class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Suggestion


class UserSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = User
		fields = ('url', 'username', 'events', 'invites', 'suggestions')
		
