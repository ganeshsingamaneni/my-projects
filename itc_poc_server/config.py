from flask import Flask
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql://root:Welcome@123@104.199.146.29/itcpocserver"


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.init_app(app)