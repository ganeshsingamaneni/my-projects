from datetime import datetime
from flask import make_response, request
from models.input_master import Input_Master
from schemas.input_master_schema import Input_Master_Get_schema,Input_Master_schema
from config import *
from sqlalchemy import and_, or_, not_
import decimal
from flask_restful import Api, Resource
import os
from os.path import expanduser
import datetime
import logging
import logging
import logging.config
import yaml

home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/input_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postInput_master')
loggers = logging.getLogger("Input_masterconsole")


class Add_Input_Master(Resource):
    ''' This call is to add new  Input Master details and get all the  input Master details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the  input Master details in the database'''
        try:
            categories = db.session.query(Input_Master).order_by(Input_Master.id).all()
            if categories:
                data_schema = Input_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of Input Master details is success")
                # loggers.info("getting data of account details is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on  Input  Master")    
            return({"success": False, "message": "no data is available on  Input  Master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the  Input Master details into database'''
        try:
            da = request.get_json()
            dit = {key: value for key, value in da.items()}
         
            schema = Input_Master_schema()
            new_hotel = schema.load(dit, session=db.session)
            new_hotel.updatedAt = datetime.datetime.utcnow()
            db.session.add(new_hotel)
            db.session.commit()
            logger.info("succesfully added data to Input Master")
            return ({"success": True, "data": "succesfully posted"})
            
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Input_Master_Details_By_Id(Resource):
    ''' This call is to get and update Input Masters details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Input Master details based on id'''
        try:
            account = db.session.query(Input_Master).filter(
                Input_Master.id == id).first()
            if account:
                data_schema = Input_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of input master details on id is success")
                # loggers.info("getting data of input master details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Input master id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Input Master details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Input_Master).filter(
                Input_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Input_Master).filter_by(id=id).one()
                schema = Input_Master_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on id ")
                loggers.info("data updated successfully based on Input master id ")
                return({"success": True, "data": data})
            else:
                logger.info("input Master data not updated")
                return({"success": False, "message": "not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


