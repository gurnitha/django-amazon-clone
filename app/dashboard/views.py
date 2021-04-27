# app/dashboard/views.py
from django.shortcuts import render

# Create your views here.
def adminHome(request):
	return render(request, 'dashboard/home.html')

def adminLogin(request):
	return render(request, 'dashboard/login.html')

def adminLoginProcess(request):
	return render(request, 'dashboard/login_process.html')