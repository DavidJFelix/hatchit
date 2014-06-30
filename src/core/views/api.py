from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import Suggestion, Event, Invite
from ..serializers import UserSerializer, SuggestionSerializer, EventSerializer, InviteSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class SuggestionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Event.objects.all()
	serializer_class = SuggestionSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Event.objects.all()
	serializer_class = EventSerializer


class InviteViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Invite.objects.all()
	serializer_class = InviteSerializer
