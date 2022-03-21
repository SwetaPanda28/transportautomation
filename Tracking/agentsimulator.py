__author__ = 'vivek'

import requests
import datetime
import json
url = 'http://localhost:8000/thermalImagingData/10'
payload = {'temp': 1,
 'co2': 2,
 'humidity': 3,
  'image_link': 4,
   'video_link': 5, 
   'accelerometer': 200,
    'mo2': 7, 
    'mo3': 8,
    'mo4' : 'sweta_id',
     'mo5' : 0,
      'mo6' : 0 , 
      'mo7': 0,
      'mo8': 0,
      'mo9': 5,
      'mo135': 9,
      }

# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data ( Working as well)
#r = requests.post(url, data=payload)

# POST with JSON

r = requests.post(url, data=payload)

# Response, status etc
print(r.text) 
print(r.status_code)
