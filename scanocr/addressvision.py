import base64
import requests
import io
import os
import json
from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson
import re
from werkzeug.utils import secure_filename
import datetime
from datetime import date
from PIL import Image
from pprint import pprint
import cv2
from os.path import join
from collections import defaultdict,OrderedDict
#from cropaadhar import cropaddress
from difflib import get_close_matches


def detect_text(image_file):
#    crop=cropaddress(image_file)
    unlike=['UNIQUE IDENTIFICATION AUTHORITY','OF INDIA','uidai','INDIA','India','www','I','1B 1ST','MERI PEHACHAN','1E 1B','MERA AADHAAR','Unique Identification Authority','of India','UNQUE IDENTIFICATION AUTHORITY','1800 180 1947','Admi ka Adhikar','w','ww','S','s','1800 180 17','WWW','dai','uidai','Address','1809 180 1947','help','AADHAAR','160 160 1947','Aadhaar','180 18167','gov in']
    unwanted = 'UNIQUE IDENTIFICATION AUTHORITY OF INDIA'
    duplicate = 'Unique Identification Authority of India'
    with open(image_file, 'rb') as image:
         base64_image = base64.b64encode(image.read()).decode()
    url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAOztXTencncNtoRENa1E3I0jdgTR7IfL0'
    header = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                'type': 'DOCUMENT_TEXT_DETECTION',
                'maxResults': 100,
            }],
            "imageContext":{
            "languageHints":["en-t-iO-handwrit"]
            }
        }]
    }
    response = requests.post(url, headers=header, json=body).json()
    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
    block=str(text).split('\n')
    # print("fulltext:",text)
    #print("address:",block)
    reverse = block[::-1]
    care_of=re.compile('S/O')
    house_name=care_of.findall(text)
    if len(house_name)==0:
        care_of=re.compile('D/O')
        house_name=care_of.findall(text)
    if len(house_name)==0:
        care_of=re.compile('/O')
        house_name=care_of.findall(text)
    # print(".........:",house_name)
#    base=re.findall(r'\s(\w+ \w+ \w+|\w+ \w+|\d+\-\d+[A-Z]+|\d{6}|[a-zA-Z]+ [a-zA-Z]+|\w+ \w+|[a-zA-Z]+|\d{2}\-\d{3}/\[a-zA-Z]/+|[a-z]\/[a-z]|\d+\-\d+|\d+\-\d+\/[a-zA-Z]|\d+\/[a-zA-Z]|\d+\/\d+|\d+\-\d+\-\d+)',text)
#    print("base:",base)
    comp=re.compile('(\w+ \w+ \w+|\w+ \w+|\d+\-\d+[A-Z]+|[A-Z]\/O|\d{6}|[a-zA-Z]+ [a-zA-Z]+|\w+ \w+|[a-zA-Z]+|\d{2}\-\d{3}/\[a-zA-Z]/+|[a-z]\/[a-z]|\d+\-\d+|\d+\-\d+\/[a-zA-Z]|\d+\/[a-zA-Z]|\d+\/\d+|\d+\-\d+\-\d+)')
    base=comp.findall(text)
    # print("abc:",base)

    modified = [ x for x in base if x not in unlike]
    fun = [y for y in modified if len(y) != 1 ]
    done = fun[-1]
    # print("xkdvjbdkjfb:",fun,done)
    check_element =fun[0].isalpha()
    # print("jskd:",check_element)
    if check_element is False:
        fun=fun[1:]
    getting_address=fun
    # print("check_element:",fun)
    if fun[0] in unwanted:
        fun = fun[1:]
    else:
        # print("checking")
        if fun[0] in duplicate:
            fun = fun[1:]
    if len(done)>6:
        fun=[x for x in fun if x not in done]
        # print("dfkvbsdkfb:",fun)
    # print("done:",done)
    address=fun
    # print("address_data:",address)
    if fun[0].isdigit():
        #if len(fun[-1])>6:
        address=fun[1:]
    # print("beforeaddress:",address)
    if fun[0].isalnum():
        address=fun[1:]
    # print("cropaddress:",address)
    if len(house_name)>=1:
        address.insert(0,house_name[0])
    # print("modified:",modified)
    # print("fundata:",fun)
    address=address[::-1]
    unique_list = list(OrderedDict((element, None) for element in address))
    unique_list=[x for x in unique_list for y in unlike if y not in x ]
    unique_list = list(OrderedDict((element, None) for element in unique_list))
    # print("unique_list:",unique_list[::-1])
    # print("getting_address:",getting_address)
    address=unique_list[::-1]
    removedigit = re.search(r'(\d+)',address[0])
    # print("removedigit:",removedigit)
    if removedigit:
        address=address[1:]
    for y in address:
        removesymbol =re.search(r'(\d{6}|[a-zA-Z0-9-/]+)',y)
        if removesymbol is None:
            address=[x for x in address if x!=y]
        # print("removesymbol:",removesymbol)
    for y in address[::-1]:
        a=get_close_matches(y,unlike)
        if len(a)==1:
            entry=a[0]
            # print("closed matches:",a[0])
            address.remove(y)
    address=[x for x in address if len(x)>2]
    # print("final address:",address)

    pin=re.compile('\d{6}')
    code=pin.findall(text)
    # print("code:",code)
    return address
detect_text('/home/ganesh/Downloads/2019-02-06-125458.jpg')
