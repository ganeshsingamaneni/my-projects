from datetime import datetime
from flask import make_response, request
from models.financial_year_master import Financial_Year_Master
from schemas.financial_year_master_schema import Financial_Year_Master_Get_schema,Financial_Year_Master_schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/financial_year.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postfinancialyear')
loggers = logging.getLogger("financialyearconsole")


class Add_New_Financial_year_Master(Resource):
    ''' This call is to add new Financial_year_Master  details and get all the Financial_year_Master  details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Financial_year_Master  details in the database'''
        try:
            categories = db.session.query(Financial_Year_Master).order_by(Financial_Year_Master.id).all()
            if categories:
                data_schema = Financial_Year_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of Financial_year_Master details is success")
                # loggers.info("getting data of account details is success")
                return ({"success": True, "data": data})
            return({"success": False, "message": "no data is available on Financial_year_Master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the  Financial_year_Master details into database'''
        try:
            da = request.get_json()
            code = da['financial_year_code']
            name = da['financial_year_name']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(Financial_Year_Master).filter(or_(
                Financial_Year_Master.financial_year_code==code,Financial_Year_Master.financial_year_name==name)).one_or_none()
            if existing_one is None:
                schema = Financial_Year_Master_schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                new = db.session.query(Financial_Year_Master).filter(
                Financial_Year_Master.financial_year_code == code).all()
                new_sechema = Financial_Year_Master_Get_schema(many=True)
                data = new_sechema.dump(new)
                logger.info("Financial_year_Master Details posted succesfully")
                # loggers.info("Financial_year_Master Details posted succesfully")
                return ({"success": True, "data": data})
            else:
                return ({"success": False, "message": "Financial_year_Master  code or name already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Financial_year_Master_Details_By_Id(Resource):
    ''' This call is to get and update  Financial_year_Master details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Financial_year_Master  details based on id'''
        try:
            account = db.session.query(Financial_Year_Master).filter(
                Financial_Year_Master.id == id).first()
            if account:
                data_schema = Financial_Year_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Financial_year_Master details on id is success")
                # loggers.info("getting data of Financial_year_Master details on id is success")
                return ({"success": True, "data": data})
            loggers.info("no data is available on Financial_year_Master id")    
            return({"success": False, "message": "no data is available on  Financial_year_Master id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Financial_year_Master  details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Financial_Year_Master).filter(
                Financial_Year_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Financial_Year_Master).filter_by(id=id).one()
                schema = Financial_Year_Master_schema()
                data = schema.dump(account_detail)
                logger.info(" Financial_year_Master data updated successfully based on id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.warning("Financial_year_Master data not updated")
                return({"success": False, "message": "Hotel data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


