from datetime import datetime
from flask import make_response,abort,request
from models.persondetails import Passport_Details
from models.scandetaillog import Detailslog
from schemas.passport import PassportSchema, GetPassportSchema
from schemas.detailslogschema import DetailslogSchema,GetDetailslogSchema
from config import db,basedir
from flask_restful import reqparse, abort, Api, Resource
import os
import logging, logging.config, yaml
import pathlib




CONFIG_PATH = os.path.join(basedir,'loggeryaml/passportlogger.yaml')




logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('postpassport')


CONFIG=os.path.join(basedir,'loggeryaml/persondetailslogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG)))
details_logger = logging.getLogger('postpersondetails')

class GetPassportDetails(Resource):
    def __init__(self):
        pass
    def get(self):
        try:
            obj=db.session.query(Passport_Details).order_by(Passport_Details.id).all()
            if obj:
                passport_schema = PassportSchema(many=True)
                data = passport_schema.dump(obj).data
                logger.info("Data has Fetched Successfully")
                return data
            else:
                logger.warning("No data is available on roles")
                return("No data is available on roles")
        except:
            raise Nodata("No data is available")

    def post(self):
        da = request.get_json()
        print("=======",da)
        name = da['Given_Name']
        Id = request.headers.get('id')

        existing = (Passport_Details.query.filter(Passport_Details.Given_Name == name).one_or_none())
        if existing is None:
            schema = PassportSchema()
            new_role = schema.load(da, session=db.session).data
            db.session.add(new_role)
            db.session.commit()
            data = schema.dump(new_role).data
            person_id=data['id']
            details = {"person_id":person_id,"created_by":Id}
            detail_schema = DetailslogSchema()
            new_log = detail_schema.load(details,session=db.session).data
            db.session.add(new_log)
            db.session.commit()
            obj = detail_schema.dump(new_log).data
            details_logger.info(obj)
            logger.info("Data added successfully to passport")
            return data, 201
        else:
            logger.warning("Passport name exists already ")
            return("Passport name exists already")
