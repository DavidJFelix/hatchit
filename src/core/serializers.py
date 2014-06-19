from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Invite, Suggestion


class EventSerializer(serializers.HyperLinkedModelSerializer):
	class Meta:
		model = Event


class InviteSerializer(serializers.HyperLinkedModelSerializer):
	class Meta:
		model = Invite


class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Suggestion


class UserSerializer(serializers.HyperlinkedModelSerializer):
	events = serializers.HyperlinkedRelatedField(view_name='event-detail', many=True)
	invites = serializers.HyperlinkedRelatedField(view_name='invite-detail', many=True)
	suggestions = serializers.HyperlinkedRelatedField(view_name='suggestion-detail', many=True)
	
	class Meta:
		model = User
		fields = ('url', 'username', 'events', 'invites', 'suggestions')
		
