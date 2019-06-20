from datetime import datetime
from flask import make_response,abort,request
from config import db,basedir
from flask_restful import reqparse, abort, Api, Resource
import os
import logging, logging.config, yaml
import base64
from os.path import expanduser
from datetime import date, datetime
from scan_aadhar import qr_scan
from face_detect import detect_faces
from aadharvision import detect_text

home = expanduser('~')
#print("home////////////",home)
date = str(date.today())





CONFIG_PATH = os.path.join(basedir,'loggeryaml/aadharlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('post_aadhar')



class ScanAadhar(Resource):

    def __init__(self):
          pass


    def post(self):
        try:
             file = request.form
             base=file['aadhar_image']
             #print("dfgdf:",base)
             imgdata = base64.b64decode(base)
             filename = home +'/'+'aadhar.jpeg'  # I assume you have a way of picking unique filenames
             with open(filename, 'wb') as f:
                 f.write(imgdata)
             #image = request.files['aadhar_image']
             details =None
             try:
                 print("tiger1")
                 details=qr_scan(filename)
                 print("details:",details)
             except:
                 print("xkbvdk")

             try:
                 print("tiger2")
                 details = detect_text(base)
                 print("details:",details)
             except:
                 print("tiger3")
             image_string = ' '
             try:
                 print("face_detect")
                 face = detect_faces(filename)
                 os.remove(filename)
                 with open(face, 'rb') as image:
                     image_string = base64.b64encode(image.read()).decode()
                 faceimage_size = ('{:,.0f}'.format(os.path.getsize(face)/float(1<<10))+" KB")
                 os.remove(face)
             except:
                 print("not drawn:")


             #print("sdfd:",image_string)

             if details == None:
                  logger.warning("unable to extract the details from qrcode")
                  return ({"success":False,"message":"unable to read the image, please enter the details manually"})
             elif len(details)>0:
                 details['face']=image_string
                 logger.info("Data successfully extracted from qr code")
                 return ({"success":True,"aadhar_details":details})

             #image_string = base64.b64encode(image.read()).decode()

        except IndexError as e:
            logger.warning("unable to extract the details from qrcode")
            return ({"message":"unable to read the image, please enter the details manually","success":False})
        except Exception as e:
            logger.warning("unable to extract the details from qrcode")
            return ({"message":"unable to read the image, please enter the details manually","success":False})
