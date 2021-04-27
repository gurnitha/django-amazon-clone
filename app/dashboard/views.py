# app/dashboard/views.py
from django.shortcuts import render

# Create your views here.
def admin_login(request):
	return render(request, 'dashboard/login.html')