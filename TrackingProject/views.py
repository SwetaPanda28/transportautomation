__author__ = 'vivek'


from django.http import HttpResponse
from django.shortcuts import render
import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
from django.db import connection
from django.db.models import Q
import time
from TrackingProject.models import *

from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello world")

def getBusinessVehiclesLocation(request):
    # is this function redundadnt ?
    recordList = []
    print("Will send the Json Data")
    json_data = '[{"name": "Brian", "sensor": "12"}]'
    #print "Saving Data"
    getCompanyID = Company.objects.filter(username = "vivek")[0]
    #print getCompanyID.companyid
    getImieNumber = Device.objects.filter(companyid=getCompanyID.companyid).select_related()[0]
    #print getImieNumber.imienumber

    #getTransactions = Warehouse.objects.filter(imienumber=getImieNumber.imienumber).select_related()
    getTransactions = Warehouse.objects.filter(imienumber=getImieNumber.imienumber)
    #newsletters =   Warehouse.order_by(imienumber=getImieNumber.imienumber).objects.prefetch_related('imienumber').all().order_by('insertdate')

    for i in getTransactions.iterator():
        recordList.append([i.generateddate,i.latitude,i.longitude])
        #print i.generateddate,i.latitude,i.longitude
    #print recordList

    '''
    p = Warehouse(id = 1,  insertdate=datetime.datetime.now(), generateddate=datetime.datetime.now(), latitude=123.45,longitude=124.5,imienumber= Device.objects.get(imienumber = 352887078364431))
    p.save()
    '''
    return HttpResponse(json_data)


def getGPSList(request):
    # This code returns the list of gps devices for the company
    recordList = []
    getCompanyID = Company.objects.filter(username="vivek")[0]
    #print getCompanyID.companyid
    records = Device.objects.filter(companyid=getCompanyID.companyid).select_related()
    for i in records:
        print(i.imienumber)
    #print getImieNumber.imienumber
        gps_data_list = {"imienumber" : str(i.imienumber), "vehiclename" : "Truck"}
        recordList.append(gps_data_list)

    return HttpResponse(str(recordList))


def getCurrentGPSPosition(request):
    # This method will return the
    recordList = []
    #print "Will send the Json Data"
    json_data = '[{"imie": "1234567890", "latitude": "12","longitude" : "123"}]'
    #print "Saving Data"
    getCompanyID = Company.objects.filter(username="vivek")[0]
    #print getCompanyID.companyid
    records = Device.objects.filter(companyid=getCompanyID.companyid).select_related()

    for i in records:
        print(i.imienumber)

        #Both will give same values

        #getTransactions = Warehouse.objects.filter(imienumber=i.imienumber).select_related()
        #print getTransactions

        if not Warehouse.objects.filter(imienumber=i.imienumber):
            print("No Data for %s" %(i.imienumber))
        else:
            getLastTransactions = Warehouse.objects.filter(imienumber=i.imienumber).latest('generateddate')
            #print getLastTransactions
            json_data = [{'i': str(getLastTransactions.imienumber_id), 'j': str(getLastTransactions.latitude),'k' : str(getLastTransactions.longitude)}]
            recordList.append(str(json_data))




        #print getImieNumber.imienumber

    # For all the ImieNumber, get the

    return HttpResponse(recordList)

    #newsletters =   Warehouse.order_by(imienumber=getImieNumber.imienumber).objects.prefetch_related('imienumber').all().order_by('insertdate')

def getVehicleHistory(request):
 recordList = []
 #print "Will send the Json Data"
 json_data = '[{"name": "Brian", "sensor": "12"}]'
 #print "Saving Data"

 # publication = User.objects.get(username="vivek")
 #userinfo = User.objects.filter(username="vivek").select_related()[0]
 #print userinfo

 #t = User.objects.all().select_related('companyID')
 #print "hi"

 getCompanyID = Company.objects.filter(username="vivek")[0]

 #print getCompanyID.companyid

 getImieNumber = Device.objects.filter(companyid=getCompanyID.companyid).select_related()[0]

 #print getImieNumber.imienumber

 getTransactions = Warehouse.objects.filter(imienumber=getImieNumber.imienumber).select_related()
 getTransactions = Warehouse.objects.filter(imienumber=getImieNumber.imienumber)
 #newsletters =   Warehouse.order_by(imienumber=getImieNumber.imienumber).objects.prefetch_related('imienumber').all().order_by('insertdate')

 for i in getTransactions.iterator():
     #date_time_obj = datetime.datetime.strptime(i.generateddate, '%Y-%m-%d %H:%M:%S.%f')
     json_data = {"i": str(i.generateddate), "j":i.latitude ,"k" : i.longitude }
     recordList.append(json_data)
     #print i.generateddate,i.latitude,i.longitude
 #print recordList

 return HttpResponse(str(recordList))


def getCompanyHomeGeo(request):
    recordList = []
    # This will return the home latitude and longitude for the company
    record = Company.objects.filter(username="vivek")[0]

    #print record

    json_data = [{"j": record.companybaselat, "k": record.companybaselong}]

    return HttpResponse(str(json_data))

@csrf_exempt
def gpsData(request):
    #Test Base HTML Page

    # Validate Login Here

    #If Login is successful Go to Post


    if request.method == "POST":
        print("A POST Request from a Device!")

        body_unicode = request.body.decode('utf-8')

        #print "The data is"
        #print body_unicode
        body = json.loads(body_unicode)

        #print body
        t = time.localtime()
        timestamp = time.strftime('%b-%d-%Y_%H%M%S', t)

        f = open("espdata.txt", "a")
        f.write("%s\n" %body )
        f.close()

    return HttpResponse("Hi")


def base(request):
    #Test Base HTML Page
    return render(request,'base-new.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def main_page(request):
    output = "<html><body>It is now</body></html>"
    return HttpResponse(output)

def hello(request):
    return HttpResponse("Hello world")

def index(request):
    return render(request,'base-index.html')

def login(request):
    return render(request,'login_simple.html')