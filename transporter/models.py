from django.db import models

# Create your models here.

class acceptedorder(models.Model):
    product_name=models.CharField(max_length=120,default='')
    status=models.CharField(max_length=120,default='')
    created_at=models.CharField(max_length=150,default='')
    transporter_name=models.CharField(max_length=120,default='')
    customer_name=models.CharField(max_length=120,default='')
    quantity=models.CharField(default='',max_length=120)
    price_per_kg=models.CharField(max_length=120,default=0)
    phone=models.CharField(max_length=100,default=0)
    image_1=models.ImageField(upload_to='cart/')
    fromm=models.CharField(max_length=12000,default='')
    to=models.CharField(max_length=12200,default='')
    accept_cart_id=models.CharField(max_length=2200,default='')
    accept_order_id=models.CharField(max_length=2200,default='')
    