import datetime
from flask_restful import Resource, request
from config import *
from models.pm_master import Paper_Machine_Master
from schemas.pm_master_schema import PMMasterSchema
import os
from os.path import expanduser
import datetime
import logging
import logging
import logging.config
import yaml

home = expanduser("~")
CONFIG_PATH = os.path.join(basedir, 'loggeryaml/pm_master.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('postPM_master') 
loggers = logging.getLogger("PM_masterconsole")


# Getbyid, update and Delete calls
class GetbyidUpdateDeletePMMaster(Resource):
    def __init__(self):
        pass

    # pm master get call based on id
    def get(self, id):
        try:
            get_pm = db.session.query(Paper_Machine_Master).filter(
                Paper_Machine_Master.id == id).first()
            if get_pm:
                schema = PMMasterSchema()
                data = schema.dump(get_pm)
                logger.info("succesfuly fetched the data based on paper machine master id")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this paper machine master id")
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

    # pm master update call based on id
    def put(self, id):
        try:
            pm_data = request.get_json()
            pm_data.update({"updatedAt": datetime.datetime.utcnow()})
            obj = db.session.query(Paper_Machine_Master).filter(
                Paper_Machine_Master.id == id).update(pm_data)
            if obj:
                db.session.commit()
                abc = db.session.query(Paper_Machine_Master).filter_by(
                    id=id).one()
                schema = PMMasterSchema()
                data = schema.dump(abc)
                logger.info("succesfully updated the paper machine master data")
                return {"success": True, "data": data}
            else:
                logger.info("No data is found on this paper machine master id")
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

    # pm master delete call based on id
    def delete(self, id):
        try:
            obj = db.session.query(Paper_Machine_Master).filter(
                Paper_Machine_Master.id == id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                logger.info("paper machine master deleted successfully")
                return {
                    "success": True,
                    "message": "paper machine master deleted successfully"
                }
            else:
                logger.info("No data is found on this paper machine master id")
                return ("No data is found on this id")
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }


