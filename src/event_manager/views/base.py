from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import authenticate, login

def home(request):
	return render(request, 'login.html', {})


def login_user(request):
	logout(request)
	username = ""
	password = ""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/e/')
	
	return render(request, 'login.html', {})
	
	
def register_user(request):
	pass
