from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import datetime

# Sac and Transaction codes mapping  model

class Sac_Tran_Codes_Mapping(db.Model):
    __tablename__ = "sac_tran_codes_mapping"
    id                   = db.Column(db.Integer,primary_key = True)
    descrption_name      = db.Column(db.String(220),nullable = False)
    sac_code             = db.Column(db.String(20),nullable = False)
    tran_codes           = db.Column(db.Text(),nullable = False)
    status               = db.Column(db.Boolean, default = True)
    created_at           = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at           = db.Column(db.DateTime, default = datetime.datetime.utcnow())
