from logging import PlaceHolder
from select import select
from django.db import models
from django_countries.fields import CountryField


# Create your models here.

class Register1(models.Model):
    Name=models.CharField(max_length=128)
    Email_id=models.CharField(max_length=128,blank=True)
    Phone_Number=models.PositiveIntegerField(blank=True,null=True)
    Gender= models.CharField(max_length=100)
    Flat_No=models.CharField(max_length=100,blank=True)
    Street=models.CharField(max_length=256,blank=True)
    DOB=models.DateField(null=True,blank=True)
    Country=CountryField(blank=True)
    Upload_Photo=models.ImageField(null=True,blank=True,upload_to='images/')
    




    def __str__(self):
        return self.Name
