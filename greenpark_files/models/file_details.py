from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import datetime

# Output files details mapping  model


class Files_Details(db.Model):
    __tablename__ = "files_details"
    id = db.Column(db.Integer, primary_key=True)
    Outlet_name_id = db.Column(db.Integer, db.ForeignKey('outlet_details.Outlet_id'), nullable=False)
    breakfast = db.Column(db.Integer,nullable = False)
    lunch = db.Column(db.Integer,nullable = False)
    snacks = db.Column(db.Integer,nullable = False)
    dinner = db.Column(db.Integer,nullable = False)
    total  = db.Column(db.Integer,nullable = False)
    date   = db.Column(db.String(22),nullable = False)
    day    = db.Column(db.String(22),nullable = False)
    date_time = db.Column(db.DateTime,nullable = True)
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())










