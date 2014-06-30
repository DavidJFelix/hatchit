from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import Suggestion, Event, Invite, Idea, Location
from ..serializers import UserSerializer, SuggestionSerializer, EventSerializer, InviteSerializer, LocationSerializer


class IdeaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Idea.objects.all()
	serializer_class = IdeaSerializer
	

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class SuggestionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Suggestion.objects.all()
	serializer_class = SuggestionSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class InviteViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Invite.objects.all()
	serializer_class = InviteSerializer
