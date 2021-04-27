# config/urls.py

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# app/dashboard
from app.dashboard.views import admin_login

urlpatterns = [
	# main's app path
	path('', include('app.main.urls')),

	# dashboard's app paths
    # path('admin/', admin.site.urls),
    path('admin/', admin_login, name='login'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

