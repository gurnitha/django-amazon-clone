# app/dashboard/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def adminHome(request):
	return render(request, 'dashboard/home.html')

def adminLogin(request):
	return render(request, 'dashboard/login.html')

def adminLoginProcess(request):
	# Get input from the login form
	username=request.POST.get('username')
	password=request.POST.get('password')

	# Authenticate user credentials
	user=authenticate(
		request=request,
		username=username,
		password=password)

	# If user exist
	if user is not None:
		login(request=request, user=user)
		return HttpResponseRedirect(reverse('admin_home'))
	# If user not exist
	else:
		messages.error(
			request, 'Login error! Invalid login detail!')
		return HttpResponseRedirect(reverse('admin_login'))
