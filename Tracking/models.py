from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=255)  
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)  
    country = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    numberofvehicles = models.IntegerField()
    baselat = models.FloatField()  
    baselong = models.FloatField()    

class Vehicle(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  
    #driver = models.CharField(max_length=255) 
    type = models.CharField(max_length=255)  
    milage = models.IntegerField()  
    regId = models.IntegerField()

    
class sensingdata(models.Model):
    insertdate = models.DateTimeField()  
    generateddate = models.DateTimeField()  
    latitude = models.FloatField()
    longitude = models.FloatField()
    imienumber = models.ForeignKey('Device',on_delete=models.CASCADE)


class Device(models.Model):
    deviceid= models.IntegerField()
    serialno = models.CharField(max_length=255)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)  
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE) 
    msisdn = models.BigIntegerField()