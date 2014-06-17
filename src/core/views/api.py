from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Suggestion, Event, Invite

class UserList(APIView):
	pass

class Suggestionlist(APIView):
	pass

class EventList(APIView):
	pass

class InviteList(APIView):
	pass
