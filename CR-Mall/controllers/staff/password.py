from flask import make_response,abort,request
from models import Staff
from schemas.staff import Staff_signupSchema,StaffSchema,Password_ResetSchema
from config import *
from exceptions import Nodata,PostFailed
import random
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.security import generate_password_hash,check_password_hash
import logging, logging.config, yaml


class StaffForget_Password(Resource):
    def __init__(self):
        pass

    # call to send otp when user forgot the password
    def post(self):

        da = request.get_json()
        email = da['email']
        existing_user  = db.session.query(Staff).filter(Staff.email == email).first()
        if existing_user:
            number=random.randint(1000,9999)
            obj = existing_user.email
            id = existing_user.id
            userdata = {"id":id,"Otp":number}
            index("Forgrt Password", email, 'otp for your account is :' + str(number))
            return userdata
        else:
            return("no Staff with this mailid")


class StaffReset_password(Resource):
    def __init__(self):
        pass

    # call to reset the Staff password based on user_id
    def put(self,id):

        da = request.get_json()
        password= da['password']
        password_hash = generate_password_hash(password)
        dit = {"password": password_hash}
        obj=db.session.query(Staff).filter_by(id=id).update(dit)
        if obj:
            db.session.commit()
            abc = db.session.query(Staff).filter_by(id=id).one()
            a = abc.__dict__
            schema = StaffSchema()
            email = a['email']
            index("Password Reset", email, "your password has been succesfully changed.")
            data = schema.dump(abc).data
            return data
        else:
            return("No staff is available on this id")
