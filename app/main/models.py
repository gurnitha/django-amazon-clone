# app/main/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#1 CustomUser Model
class CustomUser(AbstractUser):
    user_type_choices=(
    	(1,"Admin"),
    	(2,"Staff"),
    	(3,"Merchant"),
    	(4,"Customer")
    )
    user_type=models.CharField(
    	max_length=255,
    	choices=user_type_choices,
    	default=1)


#2 AdminUser Model
class AdminUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id=models.OneToOneField(
    	CustomUser,
    	on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


#3 StaffUser Model
class StaffUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id=models.OneToOneField(
    	CustomUser,
    	on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)


#4 MerchantUser Model
class MerchantUser(models.Model):
    auth_user_id=models.OneToOneField(
    	CustomUser,
    	on_delete=models.CASCADE)
    profile_pic=models.FileField(default="")
    company_name=models.CharField(max_length=255)
    gst_details=models.CharField(max_length=255)
    address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


#5 CustomerUser Model
class CustomerUser(models.Model):
    auth_user_id=models.OneToOneField(
    	CustomUser,
    	on_delete=models.CASCADE)
    profile_pic=models.FileField(default="")
    created_at=models.DateTimeField(auto_now_add=True)


#6 Categories Model
class Categories(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    url_slug=models.CharField(max_length=255)
    thumbnail=models.FileField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)




































































































































































































































































