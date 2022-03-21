from django.shortcuts import get_object_or_404, render,redirect
from . import models,forms
from . helper import *
from django.http import HttpResponse,HttpRequest
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

def Automobilecreation(request,company):
    print(request)
    Vehicleform=forms.VehicleForm()
    dictV={'vehicleform':Vehicleform}
    if(request.method=="POST"):
        data = request.POST.copy()
        data['company'] = company   
        vehicleobj= forms.VehicleForm(data) 
        if(vehicleobj.is_valid()):
            vehicleobj.save()
            dictV['message'] = 'Vehicle Created Successfully'
            dictV['status'] = 'success'
            
        else:
            dictV['status'] = 'success'
            dictV['message'] = vehicleobj.errors
    return render(request,'Tracking/Automobilecreation.html',dictV)

    
def listvehicle(request):
    vehicle = request.user.company.vehicle_set.all()
    dictA= {'vehicles': vehicle}
    print(dictA)
    return render(request,'Tracking/listvehicle.html',dictA)


def  listdevice(request,vehicle):
    device=models.Vehicle.objects.get(pk=vehicle).device_set.all()
    dictV ={}
    dictV['devices'] = device
    return render(request,'Tracking/listdevice.html',dictV)

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


def Devicecreation(request,vehicle):

    DeviceForm=forms.DeviceForm()
    dictV={'Deviceform':DeviceForm}
    if(request.method=="POST"):
        data=request.POST.copy()
        data['vehicle']=vehicle
        Deviceobj=forms.DeviceForm(data)
        if(Deviceobj.is_valid()):
            print("ok")
            Deviceobj.save()
            dictV['status']='success'
            dictV['message']='Device Created Successfully'
        else:
            print(Deviceobj.errors)
            dictV['status']='error'
            dictV['message']=Deviceobj.errors
    return render(request,'Tracking/Devicecreation.html',dictV)


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
                user.company = company
                user.save()

                dictV['status'] = 'success'
                dictV['message'] = 'User Created successfully'
            except Exception as e:     
                dictV['status'] = 'error'
                dictV['message'] = f'User couldn`t be created {e}'
        else:
            dictV['status'] = 'error'
            dictV['message'] = 'Please enter both username and password'
        print(dictV)
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





@csrf_exempt
def thermalImagingData(request,imei):
    data = json.dumps(request.POST)
    print(data)
    try:
        devObj = models.Device.objects.get(pk=imei)
        models.Sensingdata.objects.create(device= devObj,insertdate =datetime.datetime.now(),generateddate =datetime.datetime.now(),data=data)
    except models.Device.DoesNotExist as e:
        return HttpResponse('',status=404)
    except Exception as e:
        return HttpResponse(f'{e}',status=500)
    return HttpResponse('',status=200)



# def thermalImagingData(request,imei):
#     #Test Base HTML Page
#     # Validate Login Here
#     #If Login is successful Go to Post
#     dataBuilder = {}
#     if request.method == "POST":
#         print("A POST Request from a Device")
#         print("Will Add the data to Database")
#         # Do some logic and see if UUID is there in theDB. If yes, then only insert into the DB
#         print("Will send the Json Data")
#         #json_data = '[{"name": "Brian", "sensor": "12"}]'
#         #dataBuilder['CreateTime'] = request.POST.get('CreateTime')
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         print(body)
#         dataBuilder['UUID'] = body['UUID']
#         dataBuilder['pixel1'] = body['pixel1']
#         dataBuilder['pixel2'] = body['pixel2']
#         dataBuilder['pixel3'] = body['pixel3']
#         dataBuilder['pixel4'] = body['pixel4']
#         dataBuilder['pixel5'] = body['pixel5']
#         dataBuilder['pixel6'] = body['pixel6']
#         dataBuilder['pixel7'] = body['pixel7']
#         dataBuilder['pixel8'] = body['pixel8']
#         dataBuilder['InsertTime'] = datetime.datetime.now()

#         #d = datetime.datetime.strptim e(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%S.000Z")

#         #print dataBuilder
#         #print request.body


#         #theResponse = dbOperations.insertDoc(dataBuilder)

#         #print(theResponse)

#        # result = '{"responseData": {"data":[]}}';
#        #return JsonResponse(json.dumps(result),safe = False )
#        #return HttpResponse(json.dumps(json_data) , content_type='application/json')


#     ################## just return Some data. In the future, we can handle this in a better way with authentication ##########################
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


def sensorLinedChartData(request):
    print("Sending the Sensor Line Chart Data")
    data = [
        ['Year', 'a', 'b', 'c', 'd'],
        ['2004',  1000,      400, 1 , 2],
        ['2005',  1170,      460, 2, 3],
        ['2006',  660,       1120, 3, 4],
        ['2007',  1030,      540, 5, 5]
        ]
    return HttpResponse(json.dumps(data), content_type='application/json')
    # Go to the Database and get the Sensor Values for Sensor

def getSensorData(request,id):
    vehicle = models.Vehicle.objects.get(pk=id)
    data = []
    lowerDate = datetime.datetime.strptime('14/03/2022',r'%d/%m/%Y')
    upperDate = datetime.datetime.strptime('19/03/2022',r'%d/%m/%Y')
    for device in vehicle.device_set.all():
        for sensing  in device.sensingdata_set.filter(insertdate__gte=lowerDate,insertdate__lte=upperDate):
            data.append(  json.loads(sensing.data)   )
    print(data)
    return HttpResponse(data,content_type="application/json")