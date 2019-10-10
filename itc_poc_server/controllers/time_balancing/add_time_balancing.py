from datetime import datetime
from flask import make_response, request
from models.time_balancing import Time_Balancing
from schemas.time_balancing_schema import Time_Balancing_Schema,Time_Balancing_Get_schema
from config import *
from sqlalchemy import and_, or_, not_
from flask_restful import Api, Resource
import os
from os.path import expanduser
import datetime
import logging
import logging
import logging.config
import yaml

home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/time_balancing.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_time_balancing')
loggers = logging.getLogger("time_balancing_console")


class Add_New_Time_Balance(Resource):
    ''' This call is to add new Time_Balance details and get all the Time_Balance list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Time_Balance details in the database'''
        try:
            categories = db.session.query(Time_Balancing).order_by(Time_Balancing.id).all()
            if categories:
                data_schema = Time_Balancing_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of Time_Balance details is success")
                # loggers.info("getting data of segment master details is success")
                return ({"success": True, "data": data})
            return({"success": False, "message": "no data is available on Time_Balance"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Time_Balance details into database'''
        try:
            da = request.get_json()
            dit = {key: value for key, value in da.items()}
            # existing_one = db.session.query(Time_Balancing).filter(or_(
            #     Time_Balancing.segment_code==code,Time_Balancing.segment_name==name)).one_or_none()
            # if existing_one is None:
            schema = Time_Balancing_Schema()
            new_hotel = schema.load(dit, session=db.session)
            new_hotel.updatedAt = datetime.datetime.utcnow()
            db.session.add(new_hotel)
            db.session.commit()
            logger.info("Time Balancing Details posted succesfully")
            # loggers.info("segment master Details posted succesfully")
            return ({"success": True, "data": "Posted Siccesfully"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Time_Balancing_By_Id(Resource):
    ''' This call is to get and update Time_Balancing details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Time_Balancing details based on id'''
        try:
            account = db.session.query(Time_Balancing).filter(
                Time_Balancing.id == id).first()
            if account:
                data_schema = Time_Balancing_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Time_Balancing details on id is success")
                # loggers.info("getting data of segment master details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Time_Balancing id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Time_Balancing details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Time_Balancing).filter(
                Time_Balancing.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Time_Balancing).filter_by(id=id).one()
                schema = Time_Balancing_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.info(" Time_Balancing data not updated")
                return({"success": False, "message": "Time_Balancing data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


