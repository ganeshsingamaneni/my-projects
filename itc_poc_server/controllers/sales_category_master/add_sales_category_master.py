from datetime import datetime
from flask import make_response, request
from models.sales_category_master import Sales_Category_Master
from schemas.sales_category_master_schema import Sales_Category_Master_Get_schema,Sales_Category_Master_Schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/sales_category_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('post_sales_category_master')
loggers = logging.getLogger("sales_category_master_console")


class Add_New_Sales_Category_Master(Resource):
    ''' This call is to add new Category Master details and get all the  Sales Category Master details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Sales Category Master details in the database'''
        try:
            categories = db.session.query(Sales_Category_Master).order_by(Sales_Category_Master.id).all()
            if categories:
                data_schema = Sales_Category_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of sales_category_master details is success")
                # loggers.info("getting data of sales_category_master details is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Sales_Category_Master")    
            return({"success": False, "message": "no data is available on Sales_Category_Master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the  Sales Category Master details into database'''
        try:
            da = request.get_json()
            code = da['sales_category_code']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(Sales_Category_Master).filter(
                Sales_Category_Master.sales_category_code==code).one_or_none()
            if existing_one is None:
                schema = Sales_Category_Master_Schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                new = db.session.query(Sales_Category_Master).filter(
                Sales_Category_Master.sales_category_code == code).all()
                new_sechema = Sales_Category_Master_Get_schema(many=True)
                data = new_sechema.dump(new)
                logger.info("sales_category_master Details posted succesfully")
                # loggers.info("sales_category_master Details posted succesfully")
                return ({"success": True, "data": data})
            else:
                logger.info("Sales Category Masters code or name already exists")
                return ({"success": False, "message": "Sales Category Masters code or name already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Sales_Category_Master_Details_By_Id(Resource):
    ''' This call is to get and update Sales Category Master details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Sales Category Master details based on id'''
        try:
            account = db.session.query(Sales_Category_Master).filter(
                Sales_Category_Master.id == id).first()
            if account:
                data_schema = Sales_Category_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of sales_category_master details on id is success")
                # loggers.info("getting data of sales_category_master details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on sales_category_master id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Sales Category Master details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Sales_Category_Master).filter(
                Sales_Category_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Sales_Category_Master).filter_by(id=id).one()
                schema = Sales_Category_Master_Get_schema()
                data = schema.dump(account_detail)
                logger.info("data updated successfully based on sales_category_master id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.warning("sales_category_master data not updated")
                return({"success": False, "message": "Hotel data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


