from datetime import datetime
from flask import make_response,abort,request
from models.rolemodel import Roles
from schemas.roleschema import RoleSchema, RolesGetSchema
from config import db,basedir
from flask_restful import reqparse, abort, Api, Resource
import logging, logging.config, yaml
import os

parser = reqparse.RequestParser()

CONFIG_PATH = os.path.join(basedir,'loggeryaml/roleslogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('getupdateroles')

class GetUpdateDeleteRoles(Resource):
    def __init__(self):
        pass
    def get(self,id):
        role=db.session.query(Roles).filter(Roles.id==id).first()
        if role:
            role_schema = RoleSchema()
            data = role_schema.dump(role).data
            logger.info("Successfully data has fetched by Id")
            return data
        else:
            logger.warning("No data is found on this id")
            return ("No data is found on this id")

    # call to update the role based on id
    def put(self,id):
            obj=db.session.query(Roles).filter(Roles.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                abc=db.session.query(Roles).filter_by(id=id).one()
                schema = RoleSchema()
                data = schema.dump(abc).data
                logger.info("Data has updated successfully")
                return data
            else:
                logger.warning("No data is found on this id")
                return("No data is found on this id")


    # call to delete the role based on id
    def delete(self,id):
            obj=db.session.query(Roles).filter(Roles.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                logger.info("Role deleted successfully")
                return("Role deleted successfully")
            else:
                logger.info("No data is found on this id")
                return("No data is found on this id")
