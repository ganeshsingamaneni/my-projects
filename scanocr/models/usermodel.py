import os
from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import datetime
from sqlalchemy.orm import validates
from models.scandetaillog import Detailslog
from models.rolemodel import Roles



class User(db.Model):
    __tablename__ = "user"
    id             = db.Column(db.Integer,primary_key=True)
    first_name     = db.Column(db.String(50),nullable=True)
    role_id        = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable = True)
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
    created        = db.relationship("Detailslog", backref = db.backref("created"),lazy='dynamic',foreign_keys= 'Detailslog.created_by')
    updated        = db.relationship("Detailslog", backref = db.backref("updated"),lazy='dynamic',foreign_keys= 'Detailslog.updated_by')

    def __init__(self, email, password):
        self.email      = email
        self.password   = password
        self.created_at = datetime.datetime.now()

    @validates('email')
    def validate_email(self,key,address):
        assert '@' in address
        return address
class RevokedTokenModel(db.Model):
     __tablename__ = 'revoked_tokens'
     id = db.Column(db.Integer, primary_key = True)
     jti = db.Column(db.String(120))

     def add(self):
         db.session.add(self)
         db.session.commit()

     @classmethod
     def is_jti_blacklisted(cls, jti):
         query = cls.query.filter_by(jti = jti).first()
         return bool(query)
