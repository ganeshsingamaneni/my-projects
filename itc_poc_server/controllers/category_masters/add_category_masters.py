from datetime import datetime
from flask import make_response, request
from models.category_master import Category_Master
from schemas.category_master_schema import Category_Master_schema,Category_Master_Get_schema
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
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/category.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postcategory')
loggers = logging.getLogger("categoryconsole")


class Add_New_Category_Master(Resource):
    ''' This call is to add new Category Master details and get all the Category Master details list'''

    def __init__(self):
        pass

    def get(self):
        ''' This method will return all the Category Master details in the database'''
        try:
            categories = db.session.query(Category_Master).order_by(Category_Master.id).all()
            if categories:
                data_schema = Category_Master_Get_schema(many=True)
                data = data_schema.dump(categories)
                logger.info("getting data of Category_Master details is success")
                # loggers.info("getting data of account details is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Category_Master")    
            return({"success": False, "message": "no data is available on Category_Master"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def post(self):
        ''' This is to add the Category Master details into database'''
        try:
            da = request.get_json()
            code = da['category_code']
            name = da['category_name']
            dit = {key: value for key, value in da.items()}
            existing_one = db.session.query(Category_Master).filter(or_(
                Category_Master.category_code==code,Category_Master.category_name==name)).one_or_none()
            if existing_one is None:
                schema = Category_Master_schema()
                new_hotel = schema.load(dit, session=db.session)
                new_hotel.updatedAt = datetime.datetime.utcnow()
                db.session.add(new_hotel)
                db.session.commit()
                new = db.session.query(Category_Master).filter(
                Category_Master.category_code == code).all()
                new_sechema = Category_Master_Get_schema(many=True)
                data = new_sechema.dump(new)
                logger.info("Category_Master Details posted succesfully")
                # loggers.info("Hotel Details posted succesfully")
                return ({"success": True, "data": data})
            else:
                logger.info("Category Masters code or name already exists")
                return ({"success": False, "message": "Category Masters code or name already exists"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})


class Category_Master_Details_By_Id(Resource):
    ''' This call is to get and update Category Master details based on id'''

    def __init__(self):
        pass

    def get(self, id):
        '''This methods is to get the Category Master details based on id'''
        try:
            account = db.session.query(Category_Master).filter(
                Category_Master.id == id).first()
            if account:
                data_schema = Category_Master_Get_schema()
                data = data_schema.dump(account)
                logger.info("getting data of Category Master details on id is success")
                # loggers.info("getting data of hotel details on id is success")
                return ({"success": True, "data": data})
            logger.info("no data is available on Category Master details id")    
            return({"success": False, "message": "no data is available on id"})
        except Exception as e:
            logger.exception("Exception occured")
            return ({"success": False, "message": str(e)})

    def put(self, id):
        '''This methods is to update the Category Master details based on id '''
        try:
            da = request.get_json()
            da.update({"updatedAt":datetime.datetime.utcnow()})
            accounts = db.session.query(Category_Master).filter(
                Category_Master.id == id).update(da)
            if accounts:
                db.session.commit()
                account_detail = db.session.query(
                    Category_Master).filter_by(id=id).one()
                schema = Category_Master_Get_schema()
                data = schema.dump(account_detail)
                logger.info("Category Master details updated successfully based on id ")
                # loggers.info("data updated successfully based on id ")
                return({"success": True, "data": data})
            else:
                logger.warning("Category Master details data not updated")
                return({"success": False, "message": "Hotel data not updated"})
        except Exception as e:
            logger.exception("Exception occured")
            return({"success": False, "message": str(e)})


