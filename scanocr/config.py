import os
import connexion
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_mail import Mail, Message
from flask_jwt_extended import JWTManager

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app =connexion.App(__name__,specification_dir='')

app = connex_app.app
ma = Marshmallow(app)
db = SQLAlchemy(app)
db.init_app(app)



app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bhanuchander008@gmail.com'
app.config['MAIL_PASSWORD'] = 'abhi1015'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def index(subject, email, body):
   msg = Message(subject, sender = 'bhanuchander008@gmail.com', recipients = [email])
   msg.body = body
   mail.send(msg)
   return "Sent"



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'



class ProductionConfig(Config):
    DEBUG = False
#    print("production")


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    #print("StagingConfig")


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:Welcome@123@104.199.146.29/scandetails"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    #print("development")


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:Welcome@123@104.199.146.29/testingscan"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
#    print("testing")

config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
    )
