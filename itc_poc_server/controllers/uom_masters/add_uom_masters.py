from datetime import datetime
from flask import make_response, request
from models.uom_master import UOM_Master
from schemas.uom_schema import Uom_Master_Get_schema,Uom_Master_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/uom_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_uom_master')
loggers = logging.getLogger("uom_master_console")


class Add_New_Uom_Master(Resource):
    ''' This call is to add new Uom Master details and get all the Uom Master details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Uom Master details in the database'''
        try:
            categories = db.session.query(UOM_Master).order_by(UOM_Master.id).all()
            if categories:
                data_schema = Uom_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of Uom master details is success")
                # loggers.info("getting data of Uom master details is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Uom master")    
            return({"success": False, "message": "no data is available on Uom master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Category Master details into database'''
        try:
            da = request.get_json()
            code = da['uom_code']
            name = da['uom_name']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(UOM_Master).filter(or_(
                UOM_Master.uom_code==code,UOM_Master.uom_name==name)).one_or_none()
            if existing_one is None:
                schema = Uom_Master_Schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                new = db.session.query(UOM_Master).filter(
                UOM_Master.uom_code == code).all()
                new_sechema = Uom_Master_Get_schema(many=True)
                data = new_sechema.dump(new)
                logger.info("Uom master Details posted succesfully")
                # loggers.info("Hotel Details posted succesfully")
                return ({"success": True, "data": data})
            else:
                logger.info("Uom Masters code or name already exists")
                return ({"success": False, "message": "Uom Masters code or name already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Uom_Master_Details_By_Id(Resource):
    ''' This call is to get and update Uom Master details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the  Uom master details based on id'''
        try:
            account = db.session.query(UOM_Master).filter(
                UOM_Master.id == id).first()
            if account:
                data_schema = Uom_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Uom master details on id is success")
                # loggers.info("getting data of hotel details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Uom Master id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Category Master details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(UOM_Master).filter(
                UOM_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    UOM_Master).filter_by(id=id).one()
                schema = Uom_Master_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.info("Uom master data not updated")
                return({"success": False, "message": "Uom master data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


