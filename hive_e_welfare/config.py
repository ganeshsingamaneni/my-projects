from flask import Flask
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

connex_app = connexion.App(__name__)
app = connex_app.app

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Welcome@123@104.199.146.29/welfare_fraud"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)
ma = Marshmallow(app)
