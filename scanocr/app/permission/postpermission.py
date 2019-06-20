from datetime import datetime
from flask import make_response,abort,request
from models.permissionmodel import Permission
from schemas.permissionschema import PermissionSchema,GetPermissionSchema
from config import db,basedir
import logging, logging.config, yaml
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import and_
import os


CONFIG_PATH = os.path.join(basedir,'loggeryaml/permissionlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('postpermissions')


class Getcreatepermission(Resource):
    def __init__(self):
        pass

    # Roles get call
    def get(self):
        try:
            permission=db.session.query(Permission).order_by(Permission.id).all()
            if permission:
                permission_schema =GetPermissionSchema(many=True)
                data = permission_schema.dump(permission).data
                logger.info("Data has Fetched Successfully")
                return data
            else:
                logger.warning("No data is available on roles")
                return("No data is available on roles")
        except:
            raise Nodata("No data is available")

    # Roles post call
    def post(self):
        da = request.get_json()
        print("=======",da)
        role_id = da['role_id']
        view_name =da["view_name"]
        existing_permission = (Permission.query.filter(and_(Permission.role_id== role_id,Permission.view_name==view_name)).one_or_none())
        if existing_permission is None:
            schema = PermissionSchema()
            new_role = schema.load(da, session=db.session).data
            db.session.add(new_role)
            db.session.commit()
            data = schema.dump(new_role).data
            logger.info("Data added successfully to role")
            return data, 201
        else:
            logger.warning("Permissions name exists already ")
            return("Permissions name exists already")
