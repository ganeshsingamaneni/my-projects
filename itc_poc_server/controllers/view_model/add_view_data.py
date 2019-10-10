from datetime import datetime
from flask import make_response, request
from models.view_model import View_Model
from schemas.view_schema import View_Model_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/view_data.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_view_data')
loggers = logging.getLogger("view_data_console")


class Add_view_data(Resource):
    ''' This call is to add new view_data details and get all the Reel_Sheet_Ratio list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the view_data details in the database'''
        try:
            view = db.session.query(View_Model).order_by(View_Model.id).all()
            if view:
                data_schema = View_Model_Schema(many=True)
                data = data_schema.dump(view)
                logger.info("getting data of view data details is success")
                # loggers.info("getting data of view_data  details is success")
                return ({"success": True, "data": data})
            return({"success": False, "message": "no data is available on view data"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the view_data details into database'''
        try:
            da = request.get_json()
            code = da['machineNbr']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(View_Model).filter(
                View_Model.machineNbr==code).one_or_none()
            if existing_one is None:
                schema = View_Model_Schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                get_data = db.session.query(View_Model).filter(
                    View_Model.machineNbr==code).one_or_none()
                data_schema = View_Model_Schema()
                data = data_schema.dump(get_data)    
                logger.info("view_data Details posted succesfully")
                # loggers.info("view_data Details posted succesfully")
                return ({"success": True, "data": data})
            return ({"success": False, "message": "Machine Number already exists"})    
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class View_data_By_Id(Resource):
    ''' This call is to get and update view_data details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the view_data details based on id'''
        try:
            account = db.session.query(View_Model).filter(
                View_Model.id == id).first()
            if account:
                data_schema = View_Model_Schema()
                data = data_schema.dump(account)
                logger.info("getting data of View_Data details on id is success")
                # loggers.info("getting data of  View_Data details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on View_Data id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the View_Data details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(View_Model).filter(
                View_Model.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    View_Model).filter_by(id=id).one()
                schema = View_Model_Schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.info(" Reel_Sheet_Ratio data not updated")
                return({"success": False, "message": "View_Data data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


