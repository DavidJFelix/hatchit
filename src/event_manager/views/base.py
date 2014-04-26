from django.shortcuts import render

def home(request):
	return render(request, 'login.html', {})

	

"""def login_user(request):
	username = password = ""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				#login(re
				pass

"""
