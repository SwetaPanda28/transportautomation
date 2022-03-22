from email import charset
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)  
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)  
    country = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    baselat = models.FloatField()  
    baselong = models.FloatField()    


class Vehicle(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  
    #driver = models.CharField(max_length=255) 
    type = models.CharField(max_length=255)  
    mileage = models.IntegerField()  
    regId = models.IntegerField()

    
class Sensingdata(models.Model):
    insertdate = models.DateTimeField()  
    generateddate = models.DateTimeField()  
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    device = models.ForeignKey('Device',on_delete=models.CASCADE)
    data = models.TextField(null=True)

class Device(models.Model):
    datalogger=models.BooleanField(default=False)
    co2sensor=models.BooleanField(default=False)
    gps=models.BooleanField(default=False)
    axisaccelerometer=models.BooleanField(default=False)
    weightsensor=models.BooleanField(default=False)
    temperaturessensor=models.BooleanField(default=False)
    obdscanner=models.BooleanField(default=False)
    humiditysensor = models.BooleanField(default=False)
    serialno = models.CharField(max_length=100)
    type=models.CharField(max_length=100,null=True)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    msisdn = models.BigIntegerField()
    
class User(AbstractUser):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)

