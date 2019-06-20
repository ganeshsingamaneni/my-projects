import os
from flask import Flask
from config import *
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import datetime
from sqlalchemy.orm import validates
from models.rolemodel import Roles


class Permission(db.Model):
    __tablename__ = "permission"
    id              = db.Column(db.Integer,primary_key=True)
    GET             = db.Column(db.Boolean,default = False)
    PUT             = db.Column(db.Boolean,default = False)
    role_id         = db.Column(db.Integer,db.ForeignKey("roles.id"))
    POST            = db.Column(db.Boolean,default = False)
    view_name       = db.Column(db.String(50))
    client_viewname = db.Column(db.String(50))
    status          = db.Column(db.Boolean,default = False)
    created_at      = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    updated_at      = db.Column(db.DateTime, default = datetime.datetime.utcnow())
