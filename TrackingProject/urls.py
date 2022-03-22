from django.conf import settings
#from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from TrackingProject.views import *
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path
from .views import *
from  .views_old import *
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

# urlpatterns = patterns('',(r'^$', base),(r'index', index),(r'getVehicleLocation',getBusinessVehiclesLocation),
#                        (r'GPSList',getGPSList),(r'VehicleHistory',getVehicleHistory),
#                        (r'gpsData',gpsData),
#                        (r'CurrentGPSPosition',getCurrentGPSPosition),
#                        (r'CompanyHomeGeo',getCompanyHomeGeo),
#                        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)

urlpatterns = []
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', base, name='base'),
    path(r'getVehicleLocation',getBusinessVehiclesLocation, name='getBusinessVehiclesLocation'),
    path('Automobilecreation/<int:company>',Automobilecreation,name='Automobilecreation'),
    path('Businesscreation',Businesscreation,name='Businesscreation'),
    path('Devicecreation/<int:vehicle>',Devicecreation,name='Devicecreation'),
    path('test',test,name='test'),
    path('login',Login,name="login"),
    path('Usercreation/<int:company>/',Signin,name="Usercreation"),
    path('test2',test2,name='test2'),
    path('listbusiness',listbusiness,name='listbusiness'),
    path('listuser',listuser,name='listuser'),
    path('listvehicle',listvehicle,name='listvehicle'),
    path('listdevice/<int:vehicle>',listdevice,name='listdevice'),
    path('editbusiness/<int:company>',editbusiness,name='editbusiness'),
    path('deletebusiness/<int:company>',deletebusiness,name='deletebusiness'),
    path('index',index,name='index'),
    path('logout',signout,name='logout'),
    path('thermalImagingData/<int:imei>',thermalImagingData,name='thermalImagingData'),
    path('sensorLinedChartData',sensorLinedChartData,name='sensorLinedChartData'),
    path('getSensorData/<int:id>',getSensorData,name='getSensorData'),
    #path('SigninAdvance',SigninAdvance,name="SigninAdvance"),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)