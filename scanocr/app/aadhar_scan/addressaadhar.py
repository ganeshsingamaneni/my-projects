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
from addressvision import detect_text

home = expanduser('~')
#print("home////////////",home)
date = str(date.today())





CONFIG_PATH = os.path.join(basedir,'loggeryaml/aadharlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('addressaadhar')



class ScanAddress(Resource):

    def __init__(self):
          pass


    def post(self):
        try:
             file = request.form
             base=file['address_image']
             details=detect_text(base)
             logger.info("addres success extracted")
             return ({"success":True,"address":details})
        except Exception as e:            
            logger.warning("unable to read the image")
            return  ({"success":False,"message":"unable to read the image"})
