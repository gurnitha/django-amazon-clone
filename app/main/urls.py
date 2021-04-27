# app/main/urls.py 
from django.urls import path 
from app.main.views import HomePageView, About 

urlpatterns = [
	path('', HomePageView.as_view(), name='home'),
	path('about/', About, name='about'),
]