from flask import Flask
from config import *
from datetime import datetime
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
import datetime

# Hotel Details  model

class Hotel_Details(db.Model):
    __tablename__ = "hotel_details"
    id                   = db.Column(db.Integer,primary_key = True)
    hotel_name           = db.Column(db.String(200),nullable = True)
    email                = db.Column(db.String(220), unique = True, nullable = True)
    mobile               = db.Column(db.String(20),nullable = True)
    user_name            = db.Column(db.String(200),nullable = True)
    password             = db.Column(db.String(200),nullable = True)
    location             = db.Column(db.String(220),nullable = True)
    status               = db.Column(db.Boolean, default = True)
    created_at           = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at           = db.Column(db.DateTime, default = datetime.datetime.utcnow())


    @validates('email')
    def validate_email(self,key,address):
        assert '@' in address
        return address