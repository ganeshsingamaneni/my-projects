from datetime import datetime
from flask import make_response,abort,request
from models.rolemodel import Roles
from schemas.roleschema import RoleSchema
from config import db,basedir
import logging, logging.config, yaml
from flask_restful import reqparse, abort, Api, Resource
import os

CONFIG_PATH = os.path.join(basedir,'loggeryaml/roleslogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('postroles')


class Getcreateroles(Resource):
    def __init__(self):
        pass

    # Roles get call
    def get(self):
        try:
            role=db.session.query(Roles).order_by(Roles.id).all()
            if role:
                role_schema = RoleSchema(many=True)
                data = role_schema.dump(role).data
                logger.info("Data has Fetched Successfully")
                return data
            else:
                logger.warning("No data is available on roles")
                return("No data is available on roles")
        except:
            logger.warning("No data is available on roles")
            return ("No data is available")

    # Roles post call
    def post(self):
        da = request.get_json()
        print("=======",da)
        name = da['name']
        existing_role = (Roles.query.filter(Roles.name == name).one_or_none())
        if existing_role is None:
            schema = RoleSchema()
            new_role = schema.load(da, session=db.session).data
            db.session.add(new_role)
            db.session.commit()
            data = schema.dump(new_role).data
            logger.info("Data added successfully to role")
            return data, 201
        else:
            logger.warning("Role name exists already ")
            return("Role name exists already")
