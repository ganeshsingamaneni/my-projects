from datetime import datetime
from flask import make_response, request
from models.reel_sheet_ratio import Reel_Sheet_Ratio
from schemas.reel_sheet_ratio_schema import Reel_Sheet_Ratio_Schema,Reel_Sheet_Ratio_Get_schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/reel_sheet_ratio.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_reel_sheet_ratio')
loggers = logging.getLogger("reel_sheet_ratio_console")


class Add_Reel_Sheet_Ratio(Resource):
    ''' This call is to add new Reel_Sheet_Ratio details and get all the Reel_Sheet_Ratio list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Reel_Sheet_Ratio details in the database'''
        try:
            categories = db.session.query(Reel_Sheet_Ratio).order_by(Reel_Sheet_Ratio.id).all()
            if categories:
                data_schema = Reel_Sheet_Ratio_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of Reel_Sheet_Ratio details is success")
                # loggers.info("getting data of Reel_Sheet_Ratio  details is success")
                return ({"success": True, "data": data})
            return({"success": False, "message": "no data is available on Reel_Sheet_Ratio"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Reel_Sheet_Ratio details into database'''
        try:
            da = request.get_json()
            dit = {key: value for key, value in da.items()}
            # existing_one = db.session.query(Time_Balancing).filter(or_(
            #     Time_Balancing.segment_code==code,Time_Balancing.segment_name==name)).one_or_none()
            # if existing_one is None:
            schema = Reel_Sheet_Ratio_Schema()
            new_hotel = schema.load(dit, session=db.session)
            new_hotel.updatedAt = datetime.datetime.utcnow()
            db.session.add(new_hotel)
            db.session.commit()
            logger.info("Reel_Sheet_Ratio Details posted succesfully")
            # loggers.info("segment master Details posted succesfully")
            return ({"success": True, "data": "Posted Siccesfully"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Reel_Sheet_Ratio_By_Id(Resource):
    ''' This call is to get and update Reel_Sheet_Ratio details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Reel_Sheet_Ratio details based on id'''
        try:
            account = db.session.query(Reel_Sheet_Ratio).filter(
                Reel_Sheet_Ratio.id == id).first()
            if account:
                data_schema = Reel_Sheet_Ratio_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Reel_Sheet_Ratio details on id is success")
                # loggers.info("getting data of segment master details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Reel_Sheet_Ratio id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Reel_Sheet_Ratio details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Reel_Sheet_Ratio).filter(
                Reel_Sheet_Ratio.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Reel_Sheet_Ratio).filter_by(id=id).one()
                schema = Reel_Sheet_Ratio_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.info(" Reel_Sheet_Ratio data not updated")
                return({"success": False, "message": "Reel_Sheet_Ratio data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


