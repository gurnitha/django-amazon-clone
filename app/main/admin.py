# app/main/admin.py

from django.contrib import admin
from app.main.models import Categories,SubCategories

# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)