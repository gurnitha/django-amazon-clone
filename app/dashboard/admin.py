# app/dashboar/admin.py

from django.contrib import admin
from app.dashboard.models import Categories,SubCategories

# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)