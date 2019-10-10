from datetime import datetime
from flask import make_response, request
from models.nsr_data_information import Nsr_Data_Information
from schemas.nsr_data_information_schema import Nsr_Data_Information_Get_schema,Nsr_Data_2_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/nsr_data_information.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_nsr_data')
loggers = logging.getLogger("nsr_dataconsole")

class Add_Nsr_Data_Information(Resource):
    ''' This call is to add new Nsr_Data_Information details and get all the Nsr_Data_Information list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Nsr_Data_Information details in the database'''
        try:
            categories = db.session.query(Nsr_Data_Information).order_by(Nsr_Data_Information.id).all()
            if categories:
                data_schema = Nsr_Data_Information_Get_schema(many=True)
                data = data_schema.dump(categories)
                print(data)
                logger.info("getting data of Nsr_Data_Information details is success")
                # loggers.info("getting data of Nsr_Data_Information  details is success")
                return ({"success": True, "data": data})
            return({"success": False, "message": "no data is available on Nsr_Data_Information"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Nsr_Data_Information details into database'''
        try:
            da = request.get_json()
            dit = {key: value for key, value in da.items()}
            values = dit['data']
            for x in values:
                # print(x)
                pro_id = x['product_id']
                existing_one = db.session.query(Nsr_Data_Information).filter(Nsr_Data_Information.product_id==pro_id).first()
                if existing_one is None:
                    print(x,"////")
                    schema = Nsr_Data_2_Schema()
                    new_hotel = schema.load(x, session=db.session)
                    db.session.add(new_hotel)
                    db.session.commit()
                else:
                    print(x)
                    db.session.query(Nsr_Data_Information).filter(Nsr_Data_Information.product_id == pro_id).update(x)   
                    db.session.commit()
            logger.info("Nsr_Data_Information Details posted succesfully")
            # loggers.info("Nsr_Data_Information Details posted succesfully")
            return ({"success": True, "data": "Posted Siccesfully"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Nsr_Data_Information_By_Id(Resource):
    ''' This call is to get and update Nsr_Data_Information details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Nsr_Data_Information details based on id'''
        try:
            account = db.session.query(Nsr_Data_Information).filter(
                Nsr_Data_Information.id == id).first()
            if account:
                data_schema = Nsr_Data_Information_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Nsr_Data_Information details on id is success")
                # loggers.info("getting data of  Nsr_Data_Information details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on id")    
            return({"success": False, "message": "no data is available on Nsr_Data_Information id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Nsr_Data_Information details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Nsr_Data_Information).filter(
                Nsr_Data_Information.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Nsr_Data_Information).filter_by(id=id).one()
                schema = Nsr_Data_Information_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on Nsr_Data_Information id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.info(" Nsr_Data_Information data not updated")
                return({"success": False, "message": "Nsr_Data_Information data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


