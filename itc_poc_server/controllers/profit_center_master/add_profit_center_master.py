from datetime import datetime
from flask import make_response, request
from models.profit_center_master import Profit_Center_Master
from schemas.profit_center_master_schema import Profit_Center_Master_Get_schema,Profit_Center_Master_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/profit_center_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_profit_center_master')
loggers = logging.getLogger("profit_center_master_console")


class Add_Profit_center_Master(Resource):
    ''' This call is to add new Profit Center Master details and get all the profit center Master details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the profit center Master details in the database'''
        try:
            categories = db.session.query(Profit_Center_Master).order_by(Profit_Center_Master.id).all()
            if categories:
                data_schema = Profit_Center_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting  all data of profit center details is success")
                # loggers.info("getting data of account details is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on profit Center Master")    
            return({"success": False, "message": "no data is available on profit Center Master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Profit Center Master details into database'''
        try:
            da = request.get_json()
            code = da['profit_code']
            name = da['profit_name']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(Profit_Center_Master).filter(or_(
                Profit_Center_Master.profit_code==code,Profit_Center_Master.profit_name==name)).one_or_none()
            if existing_one is None:
                schema = Profit_Center_Master_Schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                new = db.session.query(Profit_Center_Master).filter(
                Profit_Center_Master.profit_code == code).all()
                new_sechema = Profit_Center_Master_Get_schema(many=True)
                data = new_sechema.dump(new)
                logger.info("Profit Center Master Details posted succesfully")
                # loggers.info("Profit Center Master  Details posted succesfully")
                return ({"success": True, "data": data})
            else:
                logger.info("Profit Centers Masters code or name already exists")
                return ({"success": False, "message": "Profit Centers Masters code or name already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Profit_Center_Master_Details_By_Id(Resource):
    ''' This call is to get and update Profit Centers Masters details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Profit Centers Master details based on id'''
        try:
            account = db.session.query(Profit_Center_Master).filter(
                Profit_Center_Master.id == id).first()
            if account:
                data_schema = Profit_Center_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Profit Center Master  details on id is success")
                # loggers.info("getting data of Profit Center Master  details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Profit Center Master id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Profit Centers Master details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Profit_Center_Master).filter(
                Profit_Center_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Profit_Center_Master).filter_by(id=id).one()
                schema = Profit_Center_Master_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on Profit Center Master id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.warning("Profit Center Master  data not updated")
                return({"success": False, "message": "Profit Center Master data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})

class Profit_Center_Master_Details_By_Paper_Machine_Id(Resource):
    ''' This call is to get and update Profit Centers Masters details based on Paper_Machine id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Profit Centers Master details based on Paper_Machineid'''
        try:
            account = db.session.query(Profit_Center_Master).filter(
                Profit_Center_Master.paper_machine_id == id).all()
            if account:
                data_schema = Profit_Center_Master_Get_schema(many=True)
                data = data_schema.dump(account)
                logger.info("getting data of Profit Center Master  details on id is success")
                # loggers.info("getting data of Profit Center Master  details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Profit Center Master id")    
            return({"success": False, "message": "no data is available on Profit Center Master id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})
