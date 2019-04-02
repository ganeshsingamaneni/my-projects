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
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:caratred@/crmall?unix_socket=/cloudsql/fabled-sol-222312:us-central1:flaskmall"

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
    address        = db.Column(db.Text(),nullable = True)
    gender         = db.Column(db.Enum('M','F','O'),nullable=True)
    email_otp      = db.Column(db.String(10), nullable = True)
    mobile_otp     = db.Column(db.String(10), nullable = True)
    phone_verified = db.Column(db.Boolean, default = False)
    email_verified = db.Column(db.Boolean, default = False)
    status         = db.Column(db.Boolean, default = True)
    created_at     = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at     = db.Column(db.DateTime, default = datetime.datetime.utcnow())



    def __init__(self, email, password):
        self.email      = email
        self.password   = password
        self.created_at = datetime.datetime.now()

    # it will check the mail id of the user is valid or not
    @validates('email')
    def validate_email(self,key,address):
        assert '@' in address
        return address


#Categories details table
class Categories(db.Model):
    __tablename__ = "categories"
    id         = db.Column(db.Integer, primary_key = True)
    name       = db.Column(db.String(50))
    status     = db.Column(db.Boolean, default = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())




db.create_all()
db.session.commit()
if __name__ == '__main__':
    manager.run()
