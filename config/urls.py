# config/urls.py

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# app/dashboard
from app.dashboard.views import adminHome
from app.dashboard.views import adminLogin
from app.dashboard.views import adminLoginProcess

urlpatterns = [
	# MAIN'S APP PATHS
	path('', include('app.main.urls')),

	# DASHBOARD'S APP PATHS 
    # path('admin/', admin.site.urls),
    path('admin/home', 
    	adminHome, 
    	name='admin_home'),
    path('admin/', 
    	adminLogin, 
    	name='admin_login'),
    path('admin/login_process', 
    	adminLoginProcess, 
    	name='admin_login_process'),
]

urlpatterns += static(
	settings.STATIC_URL,
	document_root=settings.STATIC_ROOT)
urlpatterns += static(
	settings.MEDIA_URL,
	document_root=settings.MEDIA_ROOT)

