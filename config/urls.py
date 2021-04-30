# config/urls.py

# Impor django modules
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# app/dashboard
from app.dashboard.views import (
    adminHome,
    adminLogin,
    adminLoginProcess,
    adminLogoutProcess,
    categoryListView,
    categoryCreateView,
    categoryUpdateView,
    subCategoryListView,
    subCategoryCreateView,
    subCategoryUpdateView,
    merchantUserListView,
    merchantUserCreateView,
    merchantUserUpdateView)

urlpatterns = [
	# MAIN'S APP PATHS
	path('', include('app.main.urls')),

	# DASHBOARD'S APP PATHS 

    # ADMIN DEFAULT
    # path('admin/', admin.site.urls),
    
    # ADMIN
    
    # Admin home
    path('admin/home', adminHome, name='admin_home'),
    # Admin login
    path('admin/', adminLogin, name='admin_login'),
    # Admin login process
    path('admin/login_process', adminLoginProcess, name='admin_login_process'),
    # Admin logout process
    path('admin/logout_process', adminLogoutProcess, name='admin_logout_process'),    

    # CATEGORIES

    # Category list
    path('admin/category/list', categoryListView.as_view(), name='category_list'),
    # Category create
    path('admin/category/create', categoryCreateView.as_view(), name='category_create'),
    # Category update
    path('admin/category/update/<slug:pk>', categoryUpdateView.as_view(), name='category_update'),
    

    # SUB CATEGORIES
    
    # Subcategory list
    path('admin/subcategory/list', subCategoryListView.as_view(), name='subcategory_list'),
    # Subcategory create
    path('admin/subcategory/create', subCategoryCreateView.as_view(), name='subcategory_create'),
    # Subcategory update
    path('admin/subcategory/update/<slug:pk>', subCategoryUpdateView.as_view(), name='subcategory_update'),


    # MERCHANT USERS

    path('admin/merchant/create', merchantUserCreateView.as_view(), name="merchant_create"),
    path('admin/merchant/list', merchantUserListView.as_view(), name="merchant_list"),
    path('admin/merchant/update/<slug:pk>', merchantUserUpdateView.as_view(), name="merchant_update"),   


]

urlpatterns += static(
	settings.STATIC_URL,
	document_root=settings.STATIC_ROOT)
urlpatterns += static(
	settings.MEDIA_URL,
	document_root=settings.MEDIA_ROOT)

