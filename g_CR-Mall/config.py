import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from flask_mail import Mail, Message
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
connex_app = connexion.App(__name__)
app = connex_app.app

db = SQLAlchemy(app)
mail = Mail(app)

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:caratred@/crmall?unix_socket=/cloudsql/fabled-sol-222312:us-central1:flaskmall"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



#---------------------------------------------------------------------------------------------------------



db.init_app(app)
ma = Marshmallow(app)
