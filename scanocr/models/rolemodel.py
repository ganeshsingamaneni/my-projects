import os
from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import datetime
from sqlalchemy.orm import validates

class Roles(db.Model):
    __tablename__ = "roles"
    id      = db.Column(db.Integer,primary_key=True)
    name    = db.Column(db.String(50),nullable=True)
    status  = db.Column(db.Boolean, default = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())

    User = db.relationship("User", backref = db.backref("Role_User"))
    perm  = db.relationship("Permission",backref = db.backref("Role_Permissions"))
