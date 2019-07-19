from datetime import datetime
from flask import make_response,request
from models.hotel_model import Hotel_Details
from schemas.hotel_schema import Hotel_Details_Schema
from config import *
from flask_restful import Api, Resource
import os,logging,sys
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from os.path import expanduser
import logging, logging.config, yaml

home = expanduser("~")
CONFIG_PATH = os.path.join(basedir,'loggeryaml/hotel_details.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
logger = logging.getLogger('posthotel')
loggers = logging.getLogger("consoleposthotel")

class Post_Hotel_Details(Resource):
    def __init__(self):
        pass
    # hotels details get call
    def get(self):
        try:
            role=db.session.query(Hotel_Details).order_by(Hotel_Details.id).all()
            if role:
                data_schema = Hotel_Details_Schema(many=True)
                data = data_schema.dump(role).data
                logger.info("getting data of hotel details is success")
                return ({"Success":True,"message":data})
            return({"Success":False,"message":"no data is available on Hotels"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"Success":False,"message":str(e)})

    # hotels details post call
    def post(self):
        try:
            da = request.get_json()
            name = da['hotel_name']
            password = da['password']
            dit = {key:value for key,value in da.items()}
            existing_one = db.session.query(Hotel_Details).filter(Hotel_Details.hotel_name == name).one_or_none()
            if existing_one is None:
                hash_password = generate_password_hash(password)
                schema = Hotel_Details_Schema()
                new_hotel = schema.load(dit, session=db.session).data
                new_hotel.password = hash_password
                db.session.add(new_hotel)
                db.session.commit()
                data = schema.dump(new_hotel).data
                logger.info("Hotel Details posted succesfully")
                return ({"Success":True,"message":data})
            else:
                return ({"Success":False,"message":"hotel already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"Success":False,"message":str(e)})



class Hotel_Details_by_id(Resource):
    def __init__(self):
        pass
    # hotels details get call
    def get(self,id):
        try:
            hotel=db.session.query(Hotel_Details).filter(Hotel_Details.id==id).first()
            if hotel:
                data_schema = Hotel_Details_Schema()
                data = data_schema.dump(hotel).data
                logger.info("getting data of hotel details on id is success")
                return ({"Success":True,"message":data})
            return({"Success":False,"message":"no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"Success":False,"message":str(e)})
    def put(self,id):
        try:
            hotel=db.session.query(Hotel_Details).filter(Hotel_Details.id==id).update(request.get_json())
            if hotel:
                db.session.commit()
                hotel_detail=db.session.query(Hotel_Details).filter_by(id=id).one()
                schema = Hotel_Details_Schema()
                data = schema.dump(hotel_detail).data
                logger.info("data updated successfully based on id ")
                return({"success":True,"data":data})
            else:
                logger.warning("address data not updated")
                return({"success":False,"message":"Hotel data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message": str(e)})
    def delete(self,id):
        try:
            hotel=db.session.query(Hotel_Details).filter(Hotel_Details.id==id).first()
            if hotel:
                db.session.delete(hotel)
                db.session.commit()
                logger.info("address deleted successfully ")
                return({"success":True,"message":"Hotel deleted successfully"})
            else:
                logger.warning("address not deleted on this id")
                return({"success":False,"message":"Hotel not deleted on this id"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success":False,"message": str(e)})

class Login(Resource):
    def __init__(self):
        pass
    # Login call
    def post(self):
        try:
            sign_in = request.get_json()
            email_id = sign_in['user_name']
            password = sign_in['password']
            email_check = db.session.query(Hotel_Details).filter(Hotel_Details.user_name == email_id).first()
            if email_check is not None:
                schema = Hotel_Details_Schema()
                hashed_password = email_check.password
                if check_password_hash(hashed_password,password):
                        return {"success":True,'message': 'login successful'}
                else:
                    return {"success":False,"message":"Invalid Password"}     
            else:
                return {"success":False,"message":"Invalid UserName"}
        except Exception as e:
            return{"success":False,"message":str(e)}    
