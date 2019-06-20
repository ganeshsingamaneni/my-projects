from datetime import datetime
from flask import make_response,abort,request
from models.permissionmodel import Permission
from schemas.permissionschema import PermissionSchema, GetPermissionSchema
from config import db,basedir
from flask_restful import reqparse, abort, Api, Resource
import logging, logging.config, yaml
import os

parser = reqparse.RequestParser()


CONFIG_PATH = os.path.join(basedir,'loggeryaml/permissionlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('getupdatepermissions')

class GetUpdateDeletePermission(Resource):
    def __init__(self):
        pass
    def get(self,id):
        obj=db.session.query(Permission).filter(Permission.id==id).first()
        if obj:
            permission_schema = GetPermissionSchema()
            data = permission_schema.dump(obj).data
            logger.debug("Successfully data has fetched by Id")
            return data
        else:
            logger.debug("No data is found on this id")
            return ("No data is found on this id")

    # call to update the role based on id
    def put(self,id):
            obj=db.session.query(Permission).filter(Permission.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                abc=db.session.query(Permission).filter_by(id=id).one()
                schema = GetPermissionSchema()
                data = schema.dump(abc).data
                logger.info("Data has updated successfully")
                return data
            else:
                logger.warning("No data is found on this id")
                return("No data is found on this id")


    # call to delete the role based on id
    def delete(self,id):
            obj=db.session.query(Permission).filter(Permission.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                logger.info("Permissions deleted successfully")
                return("Permissions deleted successfully")
            else:
                logger.info("No data is found on this id")
                return("No data is found on this id")
