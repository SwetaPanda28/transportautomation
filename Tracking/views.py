from django.shortcuts import get_object_or_404, render,redirect
from . import models,forms
from . helper import *
from django.http import HttpResponse,HttpRequest
from django.contrib.auth import authenticate,login,logout
# Create your views here.




def Automobilecreation(request,company):
    print(request)
    Vehicleform=forms.VehicleForm()
    
    company = get_object_or_404(models.Company,pk=company)
    if(request.method=="POST"):
        data = request.POST.copy()
        data['company'] = company.pk    
        vehicleobj= forms.VehicleForm(data) 
        if(vehicleobj.is_valid()):
            vehicleobj.save()
            resp=redirect('test')
            return resp
        else:
            print(vehicleobj.errors)
    return render(request,'Tracking/Automobilecreation.html',{'Vehicleform':Vehicleform})


def Businesscreation(request): 

    CompanyForm=forms.CompanyForm()
    dictV = {'Companyform':CompanyForm}
    if(request.method=="POST"):
        data = request.POST.copy()
        data['user'] = request.user.pk
        Companyobj=forms.CompanyForm(data)
        if(Companyobj.is_valid()):
            print("ok")
            Companyobj.save()
            dictV['status']='success'
            dictV['message']='Company Created Successfully'
        else:
            print(Companyobj.errors)
            dictV['status']='error'
            dictV['message']=Companyobj.errors

    return render(request,'Tracking/Businesscreation.html',dictV)


def Login(request):
    dictV ={}
    if(request.method=='POST'):
        print(request.POST)
        username=request.POST.get('username',False)
        password=request.POST.get('pass',False)
        print(username,password)
        if all((username,password)):        
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('base')

        dictV['error'] = 'invalid user credentials'
    
    return render(request,'login.html',dictV)    
    


def Signin(request,company):
    dictV = {}
    if(request.method=="POST"):
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if(username and password):
            try:
                user = models.User.objects.create_user(username = username,password=password)
                company = models.Company.objects.get(pk=company)
                company.user.add(user)
                user.save()
                company.save()
                dictV['status'] = 'success'
                dictV['message'] = 'User Created successfully'
            except Exception as e:     
                dictV['status'] = 'error'
                dictV['message'] = f'User couldn`t be created {e}'
        else:
            dictV['status'] = 'error'
            dictV['message'] = 'Please enter both username and password'
    return render(request,'signin.html',dictV)


def listuser(request):
    users=models.User.objects.all()
    dictU={'users':users}
    return render(request,'Tracking/listuser.html',dictU)

    
def listbusiness(request):
    businesses = models.Company.objects.all()
    dictV = {'businesses': businesses}
    return render(request,'Tracking/listbusiness.html',dictV)

def editbusiness(request,company):
    company = models.Company.objects.get(pk=company)
    companyForm = forms.CompanyForm(request.POST or None,instance=company)
    if companyForm.is_valid():
        companyForm.save()
        return(redirect('listbusiness'))
    else:
        print(companyForm.errors)
    return render(request,'Tracking/editBusiness.html',{'companyForm':companyForm})

def deletebusiness(request,company):
    if(request.method == 'GET'):
        confirm = bool(request.GET.get('confirm',False))
        if(confirm):
            models.Company.objects.get(pk=company).delete()
            return redirect('listbusiness')
    param={'business':company}
    return render(request,'Tracking/deleteBusiness.html',param)

    
def signout(request):
    logout(request)
    return redirect('base')