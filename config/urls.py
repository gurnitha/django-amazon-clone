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
	# main's app path
	path('', include('app.main.urls')),

	# dashboard's app paths
    # path('admin/', admin.site.urls),
    path('admin/home', adminHome, name='home'),
    path('admin/login', adminLogin, name='login'),
    path('admin/login_process', adminLoginProcess, name='login_process'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

