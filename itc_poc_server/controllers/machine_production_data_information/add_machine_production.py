from datetime import datetime
from flask import make_response, request
from models.machine_production_data_information import Machine_Production_Data_Information
from schemas.machine_production_data_information_schema import Machine_Production_Data_Information_Get_schema
from schemas.machine_production_data_information_schema import Machine_Production_Data_Information_Schema
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
# machine_product_data_information
home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/machine_product_data_information.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postmachine_product_data')
loggers = logging.getLogger("machine_product_dataconsole")

class Add_Machine_Production_Data_Information(Resource):
    ''' This call is to add new machine_product_data_information details and get all the machine_product_data_information list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the machine_product_data_information details in the database'''
        try:
            categories = db.session.query(Machine_Production_Data_Information).order_by(Machine_Production_Data_Information.id).all()
            if categories:
                data_schema = Machine_Production_Data_Information_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of machine_product_data_information details is success")
                # loggers.info("getting data of Nsr_Data_Information  details is success")
                return ({"success": True, "data": data})
            return({"success": False, "message": "no data is available on machine_product_data_information"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the machine_product_data_information details into database'''
        try:
            da = request.get_json()
            dit = {key: value for key, value in da.items()}
            values = dit['data']
            for x in values:
                pro_id = x['product_id']
                existing_one = db.session.query(Machine_Production_Data_Information).filter(Machine_Production_Data_Information.product_id==pro_id).first()
                if existing_one is None:
                    schema = Machine_Production_Data_Information_Schema()
                    new_hotel = schema.load(x, session=db.session)
                    db.session.add(new_hotel)
                else:
                    db.session.query(Machine_Production_Data_Information).filter(
                    Machine_Production_Data_Information.product_id == pro_id).update(x)
            db.session.commit()
            logger.info("machine_product_data_information Details posted succesfully")
            # loggers.info("Nsr_Data_Information Details posted succesfully")
            return ({"success": True, "data": "Posted Siccesfully"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Machine_Production_Data_Information_By_Id(Resource):
    ''' This call is to get and update machine_product_data_information details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the machine_product_data_information details based on id'''
        try:
            account = db.session.query(Machine_Production_Data_Information).filter(
                Machine_Production_Data_Information.id == id).first()
            if account:
                data_schema = Machine_Production_Data_Information_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of machine_product_data_information details on id is success")
                # loggers.info("getting data of  Nsr_Data_Information details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on id")    
            return({"success": False, "message": "no data is available on machine_product_data_information id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the machine_product_data_information details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Machine_Production_Data_Information).filter(
                Machine_Production_Data_Information.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Machine_Production_Data_Information).filter_by(id=id).one()
                schema = Machine_Production_Data_Information_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on machine_product_data_information id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.info(" machine_product_data_information data not updated")
                return({"success": False, "message": "machine_product_data_information data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


