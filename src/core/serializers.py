from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Invite, Suggestion

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		
