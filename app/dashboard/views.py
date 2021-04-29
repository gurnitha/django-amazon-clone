# app/dashboard/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
'''import login_required module to add conditionl to user login'''
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView)


# Import models
from app.dashboard.models import (
	Categories,)


# Create your views here.

# Limiting access to Admin Dashboard,
# only loggeg in user can access the admin dashboard
@login_required(login_url='/admin/')
def adminHome(request):
	return render(request, 'dashboard/home.html')

# cagegoryListView
class categoryListView(ListView):
	model=Categories
	template_name='dashboard/category_list.html'

# cagegoryListView
class categoryCreateView(CreateView):
	model=Categories
	fields="__all__"
	template_name='dashboard/category_create.html'


# adminLogin
def adminLogin(request):
	return render(request, 'dashboard/login.html')


# adminLoginProcess
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


#adminLogoutProcess
def adminLogoutProcess(request):
	logout(request)
	messages.success(request, 'Logged out successfully!')
	return HttpResponseRedirect(reverse('admin_login'))