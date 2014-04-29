from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth import authenticate, login
from event_manager.forms import UserForm

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
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		
		if user_form.is_valid():
			user = user_form.save()
			
			#TODO: see if this is needed
			user.set_password(user.pasword)
			user.save()
	else:
		user_form = UserForm()
	
	return render(request, 'base.html', {'form': user_form}) #FIXME make a login template
