from flask_restful import Resource, request
from config import *
from models.product_master import Product_Master
from schemas.product_master_schema import ProductMasterSchema,ProductMaster_Get_Schema
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

# Post and Get call of Product Master Model
class GetPostProductMaster(Resource):
    def __init__(self):
        pass

    # Product Master Get call
    def get(self):
        try:
            product = db.session.query(Product_Master).order_by(
                Product_Master.id).all()
            if product:
                schema = ProductMaster_Get_Schema(many=True)
                data = schema.dump(product)
                logger.info("succesfully fetched data of  all products")
                return ({"success": True, "data": data})
            else:
                logger.info("No data is available on Products")
                return ({
                    "success": False,
                    "message": "No data is available on Products"
                })
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }

    # Product Master Post call
    def post(self):
        try:
            get_data = request.get_json()
            schema = ProductMasterSchema()
            new_product = schema.load(get_data, session=db.session)
            db.session.add(new_product)
            db.session.commit()
            data = schema.dump(new_product)
            logger.info("successfully added data to products")
            return {"success": True, "data": data}
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }
