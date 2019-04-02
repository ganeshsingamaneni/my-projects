import os
import random
import subprocess
from flask import Flask,request,send_file
from flask_restful import reqparse, Api,Resource
# from controllers.image_download1 import Labelled_Image1
app = Flask(__name__)
api = Api(app)
from inspect import getsource
print(getsource(random.randint))
print(subprocess.__file__)
#----------------------------------------------------------------------------------------------------

class voter_card(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            #print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            image_path = image_upload + '/' + image.filename
            test = subprocess.run('cd ..;cd darknet;./darknet detector test voter_2_backup/obj.data voter_2_backup/yolo-voc.cfg voter_2_backup/yolo-voc_13000.weights '+image_path, shell=True)
            if test:
                os.remove(image_path)
                return ("ok")
        except Exception as e:
            return e
#-----------------------------------------------------------------------------------------------------
class aadhar_card(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            #print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            image_path = image_upload + '/' + image.filename
            test = subprocess.run('cd ..;cd darknet;./darknet detector test aadhaar_2_backup/obj.data aadhaar_2_backup/yolo-voc.cfg aadhaar_2_backup/yolo-voc_8100.weights '+image_path, shell=True)
            if test:
                os.remove(image_path)
                return ("ok")
        except Exception as e:
            return e
#-----------------------------------------------------------------------------------------------------
class passports(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            #print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            image_path = image_upload + '/' + image.filename
            test = subprocess.run('cd ..;cd darknet;./darknet detector test 900_passports_25-02-19/obj.data 900_passports_25-02-19/yolo-voc.2.0.cfg 900_passports_25-02-19/yolo-voc_last.weights '+image_path, shell=True)
            if test:
                os.remove(image_path)
                return ("ok")
        except Exception as e:
            return e
#-----------------------------------------------------------------------------------------------------
class business_cards(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            #print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            image_path = image_upload + '/' + image.filename
            print("1")
            test = subprocess.run('cd ..;cd darknet;./darknet detector test business_backup/obj.data business_backup/yolo-voc.cfg business_backup/yolo-voc_last.weights '+image_path, shell=True)
            if test:
                print("2")
                os.remove(image_path)
                return ("ok")
        except Exception as e:
            print("3")
            return e
#-----------------------------------------------------------------------------------------------------
class all_visas(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            #print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            image_path = image_upload + '/' + image.filename
            test = subprocess.run('cd ..;cd darknet;./darknet detector test all_visa_backup/obj.data all_visa_backup/yolo-voc.cfg all_visa_backup/yolo-voc_29400.weights '+image_path, shell=True)
            if test:
                os.remove(image_path)
                return ("ok")
        except Exception as e:
            return e
#-----------------------------------------------------------------------------------------------------
class all_cards(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            print("2")
            image_path = image_upload + '/' + image.filename
            test = subprocess.run('cd ..;cd darknet;./darknet detector test allcards_2/obj.data allcards_2/yolo-voc.cfg allcards_2/yolo-voc_11500.weights '+image_path, shell=True)
            if test:
                os.remove(image_path)
                print("3")
                return ("ok")
        except Exception as e:
            print("4")
            return e
#-----------------------------------------------------------------------------------------------------
class passport_back(Resource):
    def post(self):
        try:
            home_path = os.getcwd()
            #print("//: ",home_path)
            image = request.files['image']
            image_upload = str(home_path) + '/' + 'labelled_image'
            if not os.path.exists(image_upload):
                os.makedirs(image_upload)
            upload_folder = os.path.basename('labelled_image')
            f = os.path.join(upload_folder, image.filename)
            image.save(f)
            image_path = image_upload + '/' + image.filename
            test = subprocess.run('cd ..;cd darknet;./darknet detector test passport-back_backup/obj.data passport-back_backup/yolo-voc.cfg passport-back_backup/yolo-voc_last.weights '+image_path, shell=True)
            if test:
                os.remove(image_path)
                return ("ok")
        except Exception as e:
            return e            
api.add_resource(voter_card, '/voter_card')
api.add_resource(aadhar_card,'/aadhar_card')
api.add_resource(passports,"/passports")
api.add_resource(business_cards,"/business_cards")
api.add_resource(all_cards,"/all_cards")
api.add_resource(all_visas,'/all_visas')
api.add_resource(passport_back,'/passport_back')
#--------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug = True)
