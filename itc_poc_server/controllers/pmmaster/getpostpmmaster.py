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

# Post and Get call of PM Master Model
class GetPostPMMaster(Resource):
    def __init__(self):
        pass

    # PM Master Get call
    def get(self):
        try:
            paper_machine = db.session.query(Paper_Machine_Master).order_by(
                Paper_Machine_Master.id).all()
            if paper_machine:
                schema = PMMasterSchema(many=True)
                data = schema.dump(paper_machine)
                logger.info("succesfully fetched the paper machine master data")
                return ({"success": True, "data": data})
            else:
                logger.info("No data is available on Paper Machine")
                return ({
                    "success": False,
                    "message": "No data is available on Paper Machine"
                })
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }

    # PM Master Post call
    def post(self):
        try:
            get_data = request.get_json()
            code = get_data['paper_machine_code']
            name = get_data['paper_machine_name']
            existing_code = Paper_Machine_Master.query.filter(
                Paper_Machine_Master.paper_machine_code == code).one_or_none()
            existing_name = Paper_Machine_Master.query.filter(
                Paper_Machine_Master.paper_machine_name == name).one_or_none()
            if existing_code is None:
                if existing_name is None:
                    schema = PMMasterSchema()
                    new_pm = schema.load(get_data, session=db.session)
                    db.session.add(new_pm)
                    db.session.commit()
                    data = schema.dump(new_pm)
                    logger.info("succesfully added data to paper machine")
                    return {"success": True, "data": data}
                else:
                    logger.info("PM master name already exists")
                    return {
                        "success": False,
                        "message": "PM master name already exists"
                    }
            else:
                logger.info("PM master code already exists")
                return {
                    "success": False,
                    "message": "PM master code already exists"
                }
        except Exception as e:
            logger.exception("Exception occured")
            return {
                    "success": False,
                    "message": str(e)
                }
