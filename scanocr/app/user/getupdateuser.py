from models.usermodel import User
from schemas.userschema import UsersSchema,UsersGetSchema
from config import db,basedir
from flask_restful import Resource, reqparse
from flask import request
import logging, logging.config, yaml
import os

CONFIG_PATH = os.path.join(basedir,'loggeryaml/userlogger.yaml')

logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger(' getupdateusers')

parser = reqparse.RequestParser()
parser.add_argument('first_name', help = 'This field is mandatory', required = True)
parser.add_argument('last_name', help = 'This field is mandatory', required = True)
parser.add_argument('phone', help = 'This field is mandatory', required = True)
parser.add_argument('gender', help = 'This field is mandatory', required = True)
parser.add_argument('address', help='This field is mandatory', required = True)
parser.add_argument('role_id', help='This field is mandatory', required = True)

class GetUsers(Resource):
    def __init__(self):
        pass


    def get(self):
        user = User.query.order_by(User.id).all()
        if user:
            user_schema = UsersGetSchema(many = True)
            data = user_schema.dump(user).data
            logger.info("User data fetched succesfully based on id")
            return data
        else:
            logger.warning("Data Not Found.")
            return ("Data Not Found.")

class GetUpdateUser(Resource):
    def __init__(self):
        pass
    def get(self,id):
        user = User.query.filter(User.id == id).one_or_none()
        if user is not None:
            user_schema = UsersGetSchema()
            data = user_schema.dump(user).data
            logger.info("User data fetched succesfully based on Id")
            return data
        else:
            logger.warning("User does not exists")
            return ("User does not exists")

    # call to update the user details based on user_id
    def put(self,id):
        da = request.get_json()
        print("request data",da)
        user = db.session.query(User).filter_by(id = id).update(da)
        if user:
            db.session.commit()
            user_obj = User.query.filter(User.id == id).one()
            user_schema = UsersSchema()
            data = user_schema.dump(user_obj).data
            print("hhhhh",data)
            logger.info("User updated succesfully")
            return data
        else:
            logger.warning("User does not exists")
            return ("User does not exists")

class ActiveUsers(Resource):
    def __init__(self):
        pass
    def get(self):
        users = db.session.query(User).filter(User.status == True).all()
        print("users",users)
        if users:
            schema = UsersSchema()
            data = schema.dump(users,many=True).data
            logger.info("User fetched succesfully based on status")
            return data
        else:
            logger.warning("no users found with these status")
            return("no users found with these status")
