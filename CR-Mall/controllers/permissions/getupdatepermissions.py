from datetime import datetime
from flask_restful import reqparse, abort, Api, Resource
from config import db
from flask import request
from models import Permissions
from schemas.permissions import PermissionsSchema, PermissionsGetSchema
from exceptions import PostFailed
import os


class GetUpdatePermissions(Resource):
    def __init__(self):
        pass

    # call to get the permissions based on id
    def get(self,id):
        try:
            permission = db.session.query(Permissions).filter(Permissions.id == id).first()
            if permission:
                schema = PermissionsGetSchema()
                data = schema.dump(permission).data
                return data
            return ("no data is available with this id")
        except:
            raise PostFailed("call failed")

    # call to update the permissions based on id
    def put(self,id):
        permission = db.session.query(Permissions).filter(Permissions.id == id).update(request.get_json())
        if permission:
            db.session.commit()
            obj=db.session.query(Permissions).filter(Permissions.id==id).one()
            schema = PermissionsSchema()
            data = schema.dump(obj).data
            return data
        return("Permission with this id is not available")
