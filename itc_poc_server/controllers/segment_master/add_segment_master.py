from datetime import datetime
from flask import make_response, request
from models.segment_master import Segment_Master
from schemas.segment_master_schema import Segment_Master_Get_schema,Segment_Master_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/segment_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_segment_master')
loggers = logging.getLogger("segment_master_console")


class Add_New_Segment_Master(Resource):
    ''' This call is to add new Segment Master details and get all the Category Master details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Segment Master details in the database'''
        try:
            categories = db.session.query(Segment_Master).order_by(Segment_Master.id).all()
            if categories:
                data_schema = Segment_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of segment master details is success")
                # loggers.info("getting data of segment master details is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Segment Master")    
            return({"success": False, "message": "no data is available on Segment Master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Segment Master details into database'''
        try:
            da = request.get_json()
            code = da['segment_code']
            name = da['segment_name']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(Segment_Master).filter(or_(
                Segment_Master.segment_code==code,Segment_Master.segment_name==name)).one_or_none()
            if existing_one is None:
                schema = Segment_Master_Schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                new = db.session.query(Segment_Master).filter(
                Segment_Master.segment_code == code).all()
                new_sechema = Segment_Master_Get_schema(many=True)
                data = new_sechema.dump(new)
                logger.info("segment master Details posted succesfully")
                # loggers.info("segment master Details posted succesfully")
                return ({"success": True, "data": data})
            else:
                logger.info("Segment Masters code or name already exists")
                return ({"success": False, "message": "Segment Masters code or name already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Segment_Master_Details_By_Id(Resource):
    ''' This call is to get and update Segment Master details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Segment Master details based on id'''
        try:
            account = db.session.query(Segment_Master).filter(
                Segment_Master.id == id).first()
            if account:
                data_schema = Segment_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of segment master details on id is success")
                # loggers.info("getting data of segment master details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on segment master id ")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Segment Master details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Segment_Master).filter(
                Segment_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Segment_Master).filter_by(id=id).one()
                schema = Segment_Master_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on segment master id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.warning("segment master data not updated")
                return({"success": False, "message": "Hotel data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


