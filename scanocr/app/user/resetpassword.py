from flask import make_response,abort,request
from models.usermodel import User
from schemas.userschema import user_signupSchema,UsersSchema
from config import db,basedir
import random
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.security import generate_password_hash,check_password_hash
parser = reqparse.RequestParser()
import os
import logging, logging.config, yaml

CONFIG_PATH = os.path.join(basedir,'loggeryaml/userlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('resetpasswordusers')



class Forget_Password(Resource):
    def __init__(self):
        pass

    def post(self):

        da = request.get_json()
        email = da['email']
        print("---------------",email)
        existing_user = db.session.query(User).filter(User.email == email).first()
        if existing_user:
            number = random.randint(1000,9999)
            obj = existing_user.email
            id = existing_user.id
            userdata = {"user_id": id,"OTP":number}
            index('Verify Email', email ,'OTP for for your account is :'+ str(number))
            logger.warning(" succesfully otp sent")
            return userdata
        else:
            logger.warning(" OTP FAILED")
            return("no users with this mailid")



class Reset_password(Resource):
    def __init__(self):
        pass

    def put(self,id):
            da = request.get_json()
            password= da['password']
            password_hash = generate_password_hash(password)
            print("passkkkk",password_hash)
            dit = {"password": password_hash}
            obj=db.session.query(User).filter_by(id=id).update(dit)
            print("kkkkk",obj)
            if obj:
                db.session.commit()
                abc=db.session.query(User).filter_by(id=id).one()
                print("sssssss",abc)
                a= abc.__dict__
                print("dddddd",a)
                schema = UsersSchema()
                email = a['email']
                data = schema.dump(abc).data
                index("mail sent",email,"successfully  Reseted your password")
                logger.warning("Sucessfully password Reset")
                return data
            else:
                logger.warning(" Unsucessfully password Reset")
                return("no user is available on this id")
