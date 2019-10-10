from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import datetime
from models.file_details import Files_Details


class Outlet_Details(db.Model):
    __tablename__ = "outlet_details"
    Outlet_id = db.Column(db.Integer, primary_key=True)
    Outlet_Name = db.Column(db.String(220), nullable=False)
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    names_file = db.relationship(
        "Files_Details", backref=db.backref("files_name"), uselist=True)