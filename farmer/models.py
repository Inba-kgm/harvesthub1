from django.db import models
import os
from django.conf import settings

# Create your models here.
class farmerproduct(models.Model):
    farmer_name=models.CharField(max_length=120,default="")
    password=models.CharField(max_length=120,default="")
    image_1=models.ImageField(blank=True,null=True,upload_to='products/')
    image_2=models.ImageField(blank=True,null=True,upload_to='products/')
    image_3=models.ImageField(blank=True,null=True,upload_to='products/')
    image_4=models.ImageField(blank=True,null=True,upload_to='products/')
    product_name=models.CharField(max_length=120,default="")
    category=models.CharField(max_length=120,default="")
    amount=models.CharField(max_length=120,default="")
    per_unit=models.CharField(max_length=120,default="")
    available_quantity=models.CharField(max_length=120,default="")
    description=models.CharField(max_length=2200,default="")
    address=models.CharField(max_length=12000,default='')

    def save(self,*args,**kwargs):
        products_dir=os.path.join(settings.MEDIA_ROOT,'products')
        os.makedirs(products_dir,exist_ok=True)
        super().save(*args,**kwargs)

class acceptcart(models.Model):
    add_caartid=models.CharField(max_length=120,default='')
    created_at=models.CharField(max_length=150,default='')
    status=models.CharField(max_length=120,default='New')
    product_name=models.CharField(max_length=120,default='')
    total=models.CharField(max_length=120,default='')
    quantity=models.CharField(default='',max_length=120)
    price_per_kg=models.CharField(max_length=120,default=0)
    note=models.CharField(max_length=12000,default='Note')
    customer_name=models.CharField(max_length=120,default='')
    phone=models.CharField(max_length=100,default=0)
    image_1=models.ImageField(upload_to='cart/')
    fromm=models.CharField(max_length=12000,default='')
    to=models.CharField(max_length=12200,default='')

class farmmprofile(models.Model):
    img_1=models.ImageField(default='')
    username=models.CharField(max_length=120,default="")
    password=models.CharField(max_length=120,default="")
    email=models.CharField(max_length=120,default="")
    phone=models.CharField(max_length=120,default="")
    farmname=models.CharField(max_length=120,default='')
    location=models.CharField(max_length=2200,default='')
    date=models.DateTimeField(auto_now_add=True)