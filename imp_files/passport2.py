import base64
import requests
import io
import os
import glob

from google.cloud import vision
from google.cloud.vision import types
import pandas as pd
import csv
import json
from google.protobuf.json_format import MessageToJson
import re
#import mrz
import datetime
#from mrz.base.countries_ops import is_code
#from mrz.checker.td3 import TD3CodeChecker
img_dir = "/home/ganesh/images"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
#print("filesssssssssss: ",files)
s=[]
c=[]

for f1 in files:

    print("file: ",f1)
    with open(f1, 'rb') as image:
        base64_image = base64.b64encode(image.read()).decode()
    print("hiiiiiii")
    def detect_text():
        url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAOztXTencncNtoRENa1E3I0jdgTR7IfL0'
        header = {'Content-Type': 'application/json'}
        body = {
            'requests': [{
                'image': {
                    'content': base64_image,
                },
                'features': [{
                    'type': 'DOCUMENT_TEXT_DETECTION',
                    'maxResults': 1,
                }],
                "imageContext": {
                "languageHints": ["en-t-i0-handwrit"]
                }

            }]
        }
        response = requests.post(url, headers=header, json=body).json()
        #print ("response",response)
        text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
        #print("details",text)

        a=text.split('\n')
        #print('ppppp',a)
        d=str(text).split('\n')
        #print('jjjjj',d)
        k=a[::-1]
        #print('gggggggggg',k)
        z=str(k[2])
        x=str(k[1])
        #print("iiiiiiiiiiiiiii",z)
        #print("uuuuu",x)
        c.append(z)
        c.append(x)
        #print("f",tuple(c))
        first=c[0]
        second=c[1]
        length = (len(first)+len(second))
        #print("length of visa",length)
        #print(" first line of mrz",first)
        #print("second line of mrz",second)
        d="\n".join(tuple(c))
        #print("hhhhhhhhh",d)
        if(length==72):
          # ----------for visa---------------
          # print(MRVACodeChecker(d))
           #print("document type:",first[0])
           #print("issued state or country:",first[1])
           #print("issuing country :",first[2:5])
           ad=(first[5:]).strip('<')
           bc=ad.split('<<')
           data={"Visa_Type":first[0],"Issued_State":first[1],"Issuing_Country":first[2:5],"surname":bc[0],
                "firstname":bc[1],"personname":first[5:],"Visa_Number":second[0:9],"Nationality":second[10:13],
                "Date_of_Birth":second[13:19],"Gender":second[20],"Date_of_Expiry":second[21:27]}
           print("dataaaaa: ",data)
           for i in range(1,6):
               num = str(i)

               with open('/home/ganesh/images/visa/data'+ num +'.csv', 'w') as csv_file:
                   print("fffff: ",num)
                   #print("csv_file: ",csv_file)
                   writer = csv.writer(csv_file)
                   for key, value in data.items():
                       writer.writerow([key, value])
                       i = i+1
                       #print("okkkk")
detect_text()
