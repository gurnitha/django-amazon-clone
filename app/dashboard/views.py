# app/dashboard/views.py
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin

'''import login_required module to add conditionl to user login'''
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView)

# Import models
from app.dashboard.models import Categories
from app.dashboard.models import SubCategories


# Create your views here.

# Limiting access to Admin Dashboard,
# only loggeg in user can access the admin dashboard
@login_required(login_url='/admin/')
def adminHome(request):
	return render(request, 'dashboard/home.html')


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

# CATEGORY

# categoryListView
class categoryListView(ListView):
	model=Categories
	template_name='dashboard/category_list.html'


# categoryCreateView
class categoryCreateView(SuccessMessageMixin, CreateView):
	model=Categories
	success_message="Category added!"
	fields="__all__"
	template_name='dashboard/category_create.html'


# categoryUpdateView
class categoryUpdateView(SuccessMessageMixin, UpdateView):
	model=Categories
	success_message="Category updated!"
	fields="__all__"
	template_name='dashboard/category_update.html'



# SUB CATEGORY

# subCategoryListView
class subCategoryListView(ListView):
	model=SubCategories
	template_name='dashboard/subcategory_list.html'


# subCategoryCreateView
class subCategoryCreateView(SuccessMessageMixin, CreateView):
	model=SubCategories
	success_message="Category added!"
	fields="__all__"
	template_name='dashboard/subcategory_create.html'


# subCategoryUpdateView
class subCategoryUpdateView(SuccessMessageMixin, UpdateView):
	model=SubCategories
	success_message="Category updated!"
	fields="__all__"
	template_name='dashboard/subcategory_update.html'