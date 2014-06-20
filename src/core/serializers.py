from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Invite, Suggestion, Location


class EventSerializer(serializers.HyperLinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	invites = serializers.HyperlinkedRelatedField(view_name='invite-detail', many=True)
	
	class Meta:
		model = Event


class IdeaSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	suggestions = serializers.HypperlinkedRelatedField(view_name='suggestion-detail', many=True)
	
	class Meta:
		model = Idea

class InviteSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.Field(source='user.username')
	event = serializers.Field(source='event.description')
	
	class Meta:
		model = Invite


class LocationSerializer(serializers.HyperlinkedModelSerializer):
	events = serializers.HyperlinkedRelatedField(view_name='event-detail', many=True)
	suggestions = serializers.HyperlinkedRelatedField(view_name='suggestion-detail', many=True)
	
	class Meta:
		model = Location
		fields = ('url', 'x', 'y')

class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.Field(source='owner.username')
	
	class Meta:
		model = Suggestion


class UserSerializer(serializers.HyperlinkedModelSerializer):
	ideas = serializers.HyperlinkedRelatedField(view_name='idea-detail', many=True)
	events = serializers.HyperlinkedRelatedField(view_name='event-detail', many=True)
	invites = serializers.HyperlinkedRelatedField(view_name='invite-detail', many=True)
	suggestions = serializers.HyperlinkedRelatedField(view_name='suggestion-detail', many=True)
	
	class Meta:
		model = User
		fields = ('url', 'username', 'events', 'invites', 'suggestions')
		
