from django.conf import settings
#from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from TrackingProject.views import *
from django.urls import include, re_path
from django.contrib import admin
from django.urls import path

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
    path('', base, name='base'),
    path(r'getVehicleLocation',getBusinessVehiclesLocation, name='getBusinessVehiclesLocation')
]