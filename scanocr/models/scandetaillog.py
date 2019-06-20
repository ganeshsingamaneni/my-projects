import os
from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import datetime
from sqlalchemy.orm import validates


class Detailslog(db.Model):
   __tablename__="detailslog"
   id = db.Column(db.Integer,primary_key=True)
   person_id = db.Column(db.Integer, db.ForeignKey('passport_details.id'), nullable = False)
   created_by = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = True)
   updated_by = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = True)
   created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
   updated_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
