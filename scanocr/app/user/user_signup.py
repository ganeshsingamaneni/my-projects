from datetime import datetime
from flask import make_response,abort,request
from config import *
import logging, logging.config, yaml
from flask_restful import reqparse, abort, Api, Resource
from models.usermodel import User
from schemas.userschema import  user_signupSchema,UsersSchema
from flask import request, make_response, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash
import os
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

#import jwt
#from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


CONFIG_PATH = os.path.join(basedir,'loggeryaml/userlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH)))
logger = logging.getLogger('signup_users')

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
        email_id  = db.session.query(User).filter(User.email == email).first()
        if email_id is None:
            hash_password = generate_password_hash(password)
            schema = user_signupSchema()
            new_signup = schema.load(post_user, session = db.session).data
            new_signup.password = hash_password
            index("User Registration", email, "succesfully registered.")
            db.session.add(new_signup)
            db.session.commit()
            access_token = create_access_token(identity = email)
            refresh_token = create_refresh_token(identity = email)
            schema = UsersSchema()
            user = db.session.query(User).filter(User.email == email).one()
            data = schema.dump(new_signup).data
            logger.info("User signed up succesfully")
            return {
                'message': 'User {} was created'.format(email),
                'access_token' : access_token,
                'refresh_token': refresh_token,
                'data  '       : data
                }
        else:
            logger.warning("Email already exists")
            return ("email already exists")
