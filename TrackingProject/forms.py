from TrackingProject import models
from django import forms

class CompanyForm(forms.ModelForm):
    
    class Meta:
        model = models.Company
        exclude=[]



class VehicleForm(forms.ModelForm):
    
    class Meta:
        model = models.Vehicle
        exclude=[]


class DeviceForm(forms.ModelForm):
    
    class Meta:
        model = models.Device
        exclude=[]



class SigninUserForm(forms.ModelForm):

    class Meta:
        model = models.User
        exclude=[]



