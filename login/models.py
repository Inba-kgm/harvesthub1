from django.db import models

# Create your models here.
class cracc(models.Model):
    no_of_uploads=models.IntegerField(default=0)
    username=models.CharField(max_length=125)
    password=models.CharField(max_length=125)
    occupation=models.CharField(max_length=120)
    email=models.CharField(max_length=140)
    phone_no=models.CharField(max_length=140)
    date=models.CharField(max_length=140,default='')