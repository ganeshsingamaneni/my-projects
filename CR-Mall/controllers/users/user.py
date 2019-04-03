from models import Users
from schemas.users import UsersSchema,UsersGetSchema
from config import db
from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import jwt_required



parser = reqparse.RequestParser()
parser.add_argument('first_name', help = 'This field is mandatory', required = True)
parser.add_argument('last_name', help = 'This field is mandatory', required = True)
parser.add_argument('phone', help = 'This field is mandatory', required = True)
parser.add_argument('gender', help = 'This field is mandatory', required = True)

class GetUsers(Resource):
    def __init__(self):
        pass

    # call to get all the user details
    def get(self):
        user = Users.query.order_by(Users.id).all()
        if user:
            user_schema = UsersGetSchema(many = True)
            data = user_schema.dump(user).data
            return data
        else:
            return ("Data Not Found.")

class GetUpdateUser(Resource):
    def __init__(self):
        pass

    # call to get the user details based on user_id
    def get(self,id):
        user = db.session.query(Users).filter(Users.id == id).one_or_none()
        if user is not None:
            user_schema = UsersGetSchema()
            data = user_schema.dump(user).data
            return data
        else:
            return ("User does not exists")

    # call to update the user details based on user_id
    @jwt_required
    def put(self,id):
        data = request.get_json()
        user = db.session.query(Users).filter_by(id = id).update(data)
        if user:
            db.session.commit()
            user_obj = Users.query.filter(Users.id == id).one()
            user_schema = UsersSchema()
            data = user_schema.dump(user_obj).data
            return data
        else:
            return ("User does not exists")

class ActiveUsers(Resource):
    def __init__(self):
        pass

    # call to get the users with active status
    def get(self):
        users = db.session.query(Users).filter(Users.status == True).all()
        print("users",users)
        if users:
            schema = UsersSchema()
            data = schema.dump(users,many=True).data
            return data
        else:
            return("no users found with these status")
