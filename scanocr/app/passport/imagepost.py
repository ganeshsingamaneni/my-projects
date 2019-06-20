from datetime import datetime
from flask import make_response,abort,request
from models.persondetails import Passport_Details
from schemas.passport import PassportSchema
from config import db,basedir
from flask_restful import reqparse, abort, Api, Resource
from vision import detect_text
import os
import logging, logging.config, yaml
import base64
from face_detect import detect_faces
import os
from os.path import expanduser
from datetime import date, datetime
from exceptions import NoneType,textAnnotations
from rotateimage import rotate

home = expanduser('~')

date = str(date.today())






CONFIG_PATH = os.path.join(basedir,'loggeryaml/passportlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('imagepassports')
startlog = logging.getLogger('imagepassports')



class PostImageDetail(Resource):

    def __init__(self):
          pass


    def post(self):
        try:
             startlog.info("api call hits")
             file = request.form

             base=file['Passport_Image']

             imgdata = base64.b64decode(base)
             #header=request.headers['scan_type']
             header=file['scan_type']
             details= detect_text(base)
             if details['type']=='PASSPORT':
                 no = details['data']['Passport_Document_No']
                 unique_no = no[5:]
             elif details['type']=='VISA':
                  no=details['data']['Visa_Number']
                  unique_no = no[5:]
             filename = home +'/'+'xxxx'+str(unique_no)+'document.jpeg'  # I assume you have a way of picking unique filenames
             with open(filename, 'wb') as f:
                 f.write(imgdata)

             if header =='mobile':
                 crop = rotate(filename,unique_no)
                 fullimage_size = ('{:,.0f}'.format(os.path.getsize(filename)/float(1<<10))+" KB")
                 face=detect_faces(crop,unique_no)
                 os.remove(crop)
                 os.remove(filename)
             elif header == 'web':
                 fullimage_size = ('{:,.0f}'.format(os.path.getsize(filename)/float(1<<10))+" KB")
                 face=detect_faces(filename,unique_no)
                 os.remove(filename)

             with open(face, 'rb') as image:
                 image_string = base64.b64encode(image.read()).decode()
             faceimage_size = ('{:,.0f}'.format(os.path.getsize(face)/float(1<<10))+" KB")

             os.remove(face)

             logger.info("Data added successfully to passport")
             details['face']= image_string
             details['fullimage_size']=fullimage_size
             details['faceimage_size']=faceimage_size
             return ({"success":True,"details":details})
        except OSError as e:
            logger.warning("image not scanned properly")
            return ({"error":str(e),"success":False})
        except IndexError as e:
            logger.warning("image not scanned properly")
            return ({"error":str(e),"success":False})
        except NoneType as e:
            logger.warning("image not scanned properly")
            return ({"success":False,"message":"face was not detected properly"})
        except Exception as e:
            logger.warning("image not scanned properly")
            return ({"success":False,"message":"Text from the image not scanned properly please scan the document properly"})
        except:
            logger.warning("image not scanned properly")
            raise textAnnotations({"success":False,"message":"Text from the image not scanned properly please scan the document properly"})
