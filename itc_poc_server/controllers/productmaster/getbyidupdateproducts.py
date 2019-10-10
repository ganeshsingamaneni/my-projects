from flask_restful import Resource, request
from models.product_master import Product_Master
from schemas.product_master_schema import ProductMasterSchema,ProductMaster_Get_Schema
from models.nsr_data_information import Nsr_Data_Information
from schemas.nsr_data_information_schema import Nsr_Data_2_Schema
from config import *
import datetime
import os
from os.path import expanduser
import datetime
import logging
import logging
import logging.config
import yaml 

home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/product.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postproduct') 
loggers = logging.getLogger("productconsole")

# Getbyid, update and Delete calls
class GetbyidUpdateDeleteProductMaster(Resource):
    def __init__(self):
        pass

    # product master get call based on id
    def get(self, id):
        try:
            get_role = db.session.query(Product_Master).filter(
                Product_Master.id == id).first()
            if get_role:
                schema = ProductMaster_Get_Schema()
                data = schema.dump(get_role)
                logger.info("succesfully fetched product master data")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this product master id")
                return {
                    "success": False,
                    "message": "No data is found on this id"
                }
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }

    # Product master update call based on id
    def put(self, id):
        try:
            da = request.get_json()
            da.update({"updatedAt": datetime.datetime.utcnow()})
            obj = db.session.query(Product_Master).filter(
                Product_Master.id == id).update(da)
            if obj:
                db.session.commit()
                abc = db.session.query(Product_Master).filter_by(id=id).one()
                schema = ProductMasterSchema()
                data = schema.dump(abc)
                logger.info("succesfully updated products based on id")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this product master id")
                return {
                    "success": False,
                    "Meassage": "No data is found on this id"
                }
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }

    # Product master delete call based on id
    def delete(self, id):
        try:
            obj = db.session.query(Product_Master).filter(
                Product_Master.id == id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                logger.info("succesfully deleted product data")
                return {
                    "success": True,
                    "message": "product deleted successfully"
                }
            else:
                logger.info("No data is found on this product master id")
                return ("No data is found on this id")
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }


class Product_Master_Details_By_Profit_Center_Id(Resource):
    def __init__(self):
        pass

    # Product_Master_Details detaisl call based on Profit_Center id
    def get(self, id):
        try:
            get_role = db.session.query(Product_Master).filter(
                Product_Master.profit_center_id == id).all()
            if get_role:
                schema = ProductMaster_Get_Schema(many = True)
                data = schema.dump(get_role)
                for each in data:
                    nsrdata = db.session.query(Nsr_Data_Information).filter(Nsr_Data_Information.product_id == each['id']).first()
                    if nsrdata:
                        # if each['profit_product']['id'] == 
                        nsrschema = Nsr_Data_2_Schema()
                        nsrlastyeardata = nsrschema.dump(nsrdata)
                        each['nsrdata'] = nsrlastyeardata
                logger.info("succesfully fetched product master data based on profit center id")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this product master id")
                return {
                    "success": False,
                    "message": "No data is found on this id"
                }
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }