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


#7 SubCategories Model
class SubCategories(models.Model):
    id=models.AutoField(primary_key=True)
    category_id=models.ForeignKey(
    	Categories,
    	on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    url_slug=models.CharField(max_length=255)
    thumbnail=models.FileField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)


#8 Products Model
class Products(models.Model):
    id=models.AutoField(primary_key=True)
    url_slug=models.CharField(max_length=255)
    subcategories_id=models.ForeignKey(
    	SubCategories,
    	on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    brand=models.CharField(max_length=255)
    product_max_price=models.CharField(max_length=255)
    product_discount_price=models.CharField(max_length=255)
    product_description=models.TextField()
    product_long_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    added_by_merchant=models.ForeignKey(
    	MerchantUser,
    	on_delete=models.CASCADE)
    in_stock_total=models.IntegerField(default=1)
    is_active=models.IntegerField(default=1)


#9 ProductMedia Model
class ProductMedia(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(
    	Products,
    	on_delete=models.CASCADE)
    media_type_choice=(
    	(1,"Image"),
    	(2,"Video"))
    media_type=models.CharField(max_length=255)
    media_content=models.FileField()
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1) 


#10 ProductTransaction Model 
class ProductTransaction(models.Model):
    id=models.AutoField(primary_key=True)
    transaction_type_choices=(
    	(1,"BUY"),
    	(2,"SELL"))
    product_id=models.ForeignKey(
    	roducts,
    	on_delete=models.CASCADE)
    transaction_product_count=models.IntegerField(default=1)
    transaction_type=models.CharField(
    	choices=transaction_type_choices,
    	max_length=255)
    transaction_description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)


#11 ProductDetails Model 
class ProductDetails(models.CharField):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(
    	Products,
    	on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    title_details=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)


#12 ProductAbout Model
class ProductAbout(models.CharField):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(
    	Products,
    	on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)


#13 ProductTags Model
class ProductTags(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(
    	Products,
    	on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.IntegerField(default=1)






















































































































































































































































