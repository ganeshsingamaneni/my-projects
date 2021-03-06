from datetime import datetime
from flask import make_response,abort,request
from models import Roles
from schemas.roles import RolesSchema, RolesGetSchema
from config import db
from flask_restful import reqparse, abort, Api, Resource
from exceptions import Nodata,PostFailed
parser = reqparse.RequestParser()



class GetUpdateDeleteRoles(Resource):
    def __init__(self):
        pass

    # call to get the role details based on id
    def get(self,id):
        role=db.session.query(Roles).filter(Roles.id==id,Roles.name == 'raghu').first()
        if role:
            role_schema = RolesGetSchema()
            data = role_schema.dump(role).data
            return data
        else:
            return ("No data is found on this id")

    # call to update the role based on id
    def put(self,id):
        try:
            obj=db.session.query(Roles).filter(Roles.id==id).update(request.get_json())
            if obj:
                db.session.commit()
                abc=db.session.query(Roles).filter_by(id=id).one()
                schema = RolesSchema()
                data = schema.dump(abc).data
                return data
            else:
                return("No data is found on this id")
        except:
            raise PostFailed("call failed")

    # call to delete the role based on id
    def delete(self,id):
        try:
            obj=db.session.query(Roles).filter(Roles.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                return("Role deleted successfully")
            else:
                return("No data is found on this id")
        except:
            raise PostFailed("call failed")
