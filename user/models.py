from django.db import models

# Create your models here.
class addcart(models.Model):
    farmer_name=models.CharField(max_length=120,default='')
    total=models.CharField(max_length=120,default='')
    created_at=models.CharField(max_length=150,default='')
    status=models.CharField(max_length=120,default='New')
    product_name=models.CharField(max_length=120,default='')
    quantity=models.CharField(default='',max_length=120)
    price_per_kg=models.CharField(max_length=120,default=0)
    note=models.CharField(max_length=12000,default='Note')
    customer_name=models.CharField(max_length=120,default='')
    phone=models.CharField(max_length=100,default=0)
    image_1=models.ImageField(upload_to='cart/')
    fromm=models.CharField(max_length=12000,default='')
    destination=models.CharField(max_length=21020,default='')
    acceptcartid=models.CharField(max_length=120,default='')
    acceptedcartid=models.CharField(max_length=120,default='')

class userrprofile(models.Model):
    img_1=models.ImageField(default='')
    username=models.CharField(max_length=120,default="")
    password=models.CharField(max_length=120,default="")
    email=models.CharField(max_length=120,default="")
    phone=models.CharField(max_length=120,default="")
    location=models.CharField(max_length=10220,default='')
    date=models.CharField(max_length=2220,default='')
    
