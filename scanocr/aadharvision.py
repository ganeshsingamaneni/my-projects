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
from collections import defaultdict






def detect_text(image_file):
    #print("dflbj:",image_file)
    gender_list =['MALE','FEMALE','Male','Female']
    url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAOztXTencncNtoRENa1E3I0jdgTR7IfL0'
    header = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': image_file,
            },
            'features': [{
                'type': 'DOCUMENT_TEXT_DETECTION',
                'maxResults': 100,
            }]

        }]
    }

    response = requests.post(url, headers=header, json=body).json()
    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''

    print ("text:",text)
    gama = re.findall(r'\s(\w+\: \d{2}/\d{2}/\d{4}|\w+ \: \d{2}/\d{2}/\d{4})', text)
    match=gama[::-1]
    if len(match)>=1:
        alpha=match[0]
        dob=alpha.lstrip('DOB : ')
        print("matched date:",match)
    else:
        dob = ' '
    newlist = re.findall(r'\s(\w+\: \d{4})',text)

    if len(newlist)>=1:
        beta=newlist[0]
        yob=beta.lstrip('Birth: ')
        print("matched date:",newlist)
    else:
        yob = ' '
    print(newlist)
    block=str(text).split('\n')
    abc=[str(x) for x in block ]
    bowl = [x for x in block if x.isdigit()]
    base=re.findall(r'\s(\w+ \w+ \w+|\w+\: [0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]|\w+\: [0-9][0-9][0-9][0-9]|\d{8}\ \d{4}|\d{4}\ \d{8}|[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9]|\/ \w+|\w+ \w+|\w+ \: \d{2}/\d{2}/\d{4})',text)
    print("last two lines of passport:",base[::-1])
    hexa = [y for y in base if y!='Scanned by CamScanner' ]
    x=hexa[::-1]
    uid = x[0]
    gender = re.sub(r'[^\w]', ' ',x[1])
    gender_test= gender.lstrip(' ')
    sex = ' '
    if gender_test in gender_list:
        sex = gender_test
    name=x[3]
    birth = x[2]
    date_of_birth = birth.lstrip('birth: ')
    data={'name':name, "gender":sex, "uid":uid,"date_of_birth":dob,"year_of_birth":yob}
    print("details:",data)
    return data

#detect_text('/home/caratred/adhar/prasanth.jpg')
