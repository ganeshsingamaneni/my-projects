from config import *
from datetime import datetime
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
import os
import datetime
from sqlalchemy.orm import relationship

app = Flask(__name__)
#basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Welcome@123@104.199.146.29/cr_mall"

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

#Roles table
class Roles(db.Model):
    __tablename__ = "roles"
    id         = db.Column(db.Integer, primary_key = True)
    name       = db.Column(db.String(50))
    status     = db.Column(db.Boolean, default = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    User = db.relationship("Users", backref = db.backref("Role_user"))





#User details table
class Users(db.Model):
    __tablename__  = "users"
    id             = db.Column(db.Integer, primary_key = True)
    role_id        = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable = True)
    first_name     = db.Column(db.String(30),nullable = True)
    last_name      = db.Column(db.String(30),nullable = True)
    phone          = db.Column(db.String(10),nullable = True)
    email          = db.Column(db.String(120), unique = True, nullable = False)
    password       = db.Column(db.String(246))
    

db.create_all()
db.session.commit()
if __name__ == '__main__':
    manager.run()
