from datetime import datetime
from flask import make_response,abort,request
from models.persondetails import Passport_Details
from schemas.passport import PassportSchema
from config import db,basedir
from flask_restful import reqparse, abort, Api, Resource
from vision import detect_text
import os
import logging, logging.config, yaml
from models.scandetaillog import Detailslog
from schemas.detailslogschema import DetailslogSchema,GetDetailslogSchema

CONFIG_PATH = os.path.join(basedir,'loggeryaml/passportlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('getupdatepassports')

CONFIG=os.path.join(basedir,'loggeryaml/persondetailslogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG)))
details_logger = logging.getLogger('postpersondetails')

class GetUpdatePassport(Resource):
    def __init__(self):
        pass
    def get(self,id):
        try:
            obj = db.session.query(Passport_Details).filter(Passport_Details.id == id).first()
            if obj:
                schema = PassportSchema()
                data = schema.dump(obj).data
                logger.info("Passport data fetched succesfully based on Id")
                return data
            else:
                logger.warning("passport does not exists")
                return ("passport does not exists")
        except:
            raise PostFailed("call failed")

    # Passport update call

    def put(self,id):
        Id = request.headers.get('id')
        f = db.session.query(Passport_Details).filter(Passport_Details.id == id).update(request.get_json())
        if f:
             db.session.commit()
             obj=db.session.query(Passport_Details).filter(Passport_Details.id==id).one()
             schema = PassportSchema()
             data = schema.dump(obj).data
             person_id=data['id']
             details = {"person_id":person_id,"updated_by":Id}
             detail_schema = DetailslogSchema()
             new_log = detail_schema.load(details,session=db.session).data
             db.session.add(new_log)
             db.session.commit()
             obj = detail_schema.dump(new_log).data
             details_logger.info(obj)
             logger.info("Passport updated succesfully")
             return data
        else:
             logger.warning("passport does not exists")
             return("passport with this id is not available")
