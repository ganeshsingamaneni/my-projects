from models import Users
from schemas.users import user_signupSchema,UsersSchema
from config import *
from flask import request, make_response, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash
#from mails.signupmail import SendMail
import jwt
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


@jwt_required
def get(self):
    pass


class Signup(Resource):
    def __init__(self):
        pass

    def post(self):
        post_user = request.get_json()
        email = post_user['email']
        password = post_user['password']
        dit =  {key:value for key,value in post_user.items()}
        email_id  = db.session.query(Users).filter(Users.email == email).first()
        if email_id is None:
            hash_password = generate_password_hash(password)
            schema = user_signupSchema()
            new_signup = schema.load(dit, session = db.session).data
            new_signup.password = hash_password
            index("User Registration", email, "succesfully registered.")
            db.session.add(new_signup)
            db.session.commit()
            access_token = create_access_token(identity = email)
            refresh_token = create_refresh_token(identity = email)
            user_schema = UsersSchema()
            user = db.session.query(Users).filter(Users.email == email).one()
            data = user_schema.dump(user).data
            return {
                'message': 'User {} was created'.format(email),
                'access_token' : access_token,
                'refresh_token': refresh_token,
                'data  '       : data
                }
        else:
            return ("email already exists")
