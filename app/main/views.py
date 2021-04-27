# app/main/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'main/index.html'

def About(request):
	return render(request, 'main/about.html')	