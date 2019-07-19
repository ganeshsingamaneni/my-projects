from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import datetime

# Output files details mapping  model

class Output_files_Details(db.Model):
    __tablename__ = "output_files_detals"
    id                    = db.Column(db.Integer,primary_key = True)
    job_done              = db.Column(db.Boolean,nullable =False)
    last_run_time         = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    file_name             = db.Column(db.String(220),nullable=False)
    folio_starting_number = db.Column(db.String(220),nullable=False)
    folio_ending_number   = db.Column(db.String(220),nullable=False)
   
   
    # status               = db.Column(db.Boolean, default = True)
    # created_at           = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    # updated_at           = db.Column(db.DateTime, default = datetime.datetime.utcnow())